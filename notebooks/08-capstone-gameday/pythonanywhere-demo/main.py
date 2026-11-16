"""
DS2002 — FastAPI on PythonAnywhere.

GET /       hello
GET /time   the server clock, in UTC
GET /uva    latest Virginia men's game, read from the Yahoo Sports page

Run locally: ./start.sh  then open http://127.0.0.1:8000/docs
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException

SCHEDULE_URL = "https://sports.yahoo.com/ncaab/teams/virginia/schedule/"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}
PA_PROXY = "http://proxy.server:3128"
POSITIONS = {"G", "F", "C", "G-F", "F-G", "F-C", "C-F"}
CACHE_SECONDS = 60

app = FastAPI(
    title="DS2002 on PythonAnywhere",
    description="Hello, the server clock, and the latest Virginia men's basketball game.",
    version="0.1.0",
)

_cache: dict | None = None
_cached_at: float = 0.0


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/time")
def current_time():
    """Clock on this machine. PythonAnywhere runs in UTC, not Eastern."""
    now = datetime.now(timezone.utc)
    return {
        "timezone": "UTC",
        "iso": now.isoformat(timespec="seconds"),
        "time": now.strftime("%H:%M:%S"),
        "note": "This is the server clock, in UTC.",
    }


def _proxies() -> dict[str, str] | None:
    """Free PythonAnywhere reaches Yahoo only through its allowlist proxy."""
    proxy = os.environ.get("https_proxy") or os.environ.get("HTTPS_PROXY")
    if not proxy and os.path.exists("/etc/pythonanywhere"):
        proxy = PA_PROXY
    if not proxy:
        return None
    return {"http": proxy, "https": proxy}


def _get_html(url: str) -> str:
    attempts: list[dict[str, str] | None] = [_proxies(), {"http": PA_PROXY, "https": PA_PROXY}]
    last_error: Exception | None = None
    seen: set[str] = set()
    for proxies in attempts:
        key = "" if proxies is None else proxies["https"]
        if key in seen:
            continue
        seen.add(key)
        try:
            response = requests.get(url, headers=HEADERS, timeout=20, proxies=proxies)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            last_error = exc
    raise HTTPException(status_code=502, detail=f"Yahoo request failed: {last_error}")


def _recent_games(html: str) -> list[dict]:
    text = html.replace('\\"', '"')
    marker = '"lastGames":['
    start = text.find(marker)
    if start < 0:
        return []
    index = start + len(marker) - 1
    depth = 0
    for end in range(index, len(text)):
        if text[end] == "[":
            depth += 1
        elif text[end] == "]":
            depth -= 1
            if depth == 0:
                return json.loads(text[index : end + 1])
    return []


def _pick_game(games: list[dict]) -> dict | None:
    live = [game for game in games if game.get("status") not in {"FINAL", "PREGAME", "SCHEDULED"}]
    if live:
        return live[0]
    finals = [game for game in games if game.get("status") == "FINAL"]
    return finals[0] if finals else None


def _player_name(cell: str) -> str:
    parts = cell.split()
    if parts and parts[-1] in POSITIONS:
        parts = parts[:-1]
    return " ".join(parts)


def _table_rows(table) -> list[dict]:
    header_row = table.find("tr")
    if header_row is None:
        return []
    headers = [cell.get_text(" ", strip=True) for cell in header_row.find_all("th")]
    if "Pts" not in headers:
        return []
    name_key = headers[0]
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
        if len(cells) < len(headers):
            continue
        record = dict(zip(headers, cells))
        player = _player_name(record.get(name_key, ""))
        if not player or "total" in player.lower():
            continue
        record["player"] = player
        rows.append(record)
    return rows


def _virginia_rows(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict] = []
    for table in soup.find_all("table"):
        headers = [cell.get_text(" ", strip=True) for cell in table.find_all("th")]
        if "Stl" not in headers or "Pts" not in headers:
            continue
        heading = table.find_previous(["h2", "h3", "h4"])
        label = heading.get_text(" ", strip=True) if heading else ""
        if "Virginia" not in label:
            continue
        rows.extend(_table_rows(table))
    return rows


def _column_leader(rows: list[dict], column: str) -> dict | None:
    best: dict | None = None
    best_value = -1
    for row in rows:
        try:
            value = int(row.get(column, ""))
        except ValueError:
            continue
        if value > best_value:
            best_value = value
            best = {"player": row.get("player"), "value": value}
    return best


def _number(value) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _uva_snapshot() -> dict:
    games = _recent_games(_get_html(SCHEDULE_URL))
    game = _pick_game(games)
    if game is None:
        return {
            "team": "Virginia",
            "opponent": None,
            "status": None,
            "score": None,
            "leaders": None,
            "detail": "No completed or live game on the Yahoo schedule.",
        }

    home = (game.get("homeTeam") or {}).get("displayName") or "Home"
    away = (game.get("awayTeam") or {}).get("displayName") or "Away"
    opponent = home if away == "Virginia" else away
    rows = _virginia_rows(_get_html(game["alias"]["url"]))
    return {
        "team": "Virginia",
        "opponent": opponent,
        "status": game.get("statusDisplayName") or game.get("status"),
        "score": {
            away: _number(game.get("awayScore")),
            home: _number(game.get("homeScore")),
        },
        "leaders": {
            "points": _column_leader(rows, "Pts"),
            "rebounds": _column_leader(rows, "Reb"),
            "steals": _column_leader(rows, "Stl"),
            "blocks": _column_leader(rows, "Blk"),
        },
    }


@app.get("/uva")
def uva():
    """Latest Virginia men's game, scraped from Yahoo Sports with Beautiful Soup."""
    global _cache, _cached_at
    now = time.monotonic()
    if _cache is not None and now - _cached_at < CACHE_SECONDS:
        return _cache
    snapshot = _uva_snapshot()
    _cache = snapshot
    _cached_at = now
    return snapshot
