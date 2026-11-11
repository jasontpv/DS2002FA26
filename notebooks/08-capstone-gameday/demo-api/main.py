"""
Game Day Pulse — DS2002 FastAPI demo.

Serves read-only JSON from the capstone sample files in ../data.
Run: ./start.sh  then open http://127.0.0.1:8000/docs
"""
from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException, Query

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

_vendors: pd.DataFrame | None = None
_orders: pd.DataFrame | None = None
_zone_order_counts: dict[str, int] = {}


def _records(df: pd.DataFrame) -> list[dict]:
    """JSON-safe rows. Float columns keep NaN if you only pass None, and NaN is not valid JSON."""
    clean = df.astype(object).where(df.notna(), None)
    return clean.to_dict(orient="records")


def _load_frames() -> None:
    global _vendors, _orders, _zone_order_counts
    vendors_path = DATA_DIR / "vendor_locations.csv"
    orders_path = DATA_DIR / "gameday_orders.csv"
    if not vendors_path.is_file():
        raise FileNotFoundError(f"missing {vendors_path}")
    if not orders_path.is_file():
        raise FileNotFoundError(f"missing {orders_path}")

    _vendors = pd.read_csv(vendors_path)
    _orders = pd.read_csv(orders_path)

    merged = _orders.merge(
        _vendors[["vendor_id", "zone", "vendor_name"]],
        on="vendor_id",
        how="left",
    )
    # Orders whose vendor_id is not in the vendor file have no zone.
    # Leave them out so the response is only A, B, and C.
    _zone_order_counts = (
        merged.groupby("zone", dropna=True).size().astype(int).to_dict()
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    _load_frames()
    yield


app = FastAPI(
    title="Game Day Pulse API",
    description="DS2002 demo — read-only views of capstone vendor and order data.",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "ok", "data_dir": str(DATA_DIR)}


@app.get("/")
def root():
    return {
        "message": "Game Day Pulse API (DS2002 demo)",
        "docs": "/docs",
        "endpoints": [
            "/health",
            "/vendors",
            "/vendors/{vendor_id}",
            "/orders/summary",
            "/orders/by-zone",
        ],
    }


@app.get("/vendors")
def list_vendors(zone: str | None = Query(None, description="Filter: A, B, or C")):
    assert _vendors is not None
    df = _vendors
    if zone is not None:
        z = zone.strip().upper()
        df = df[df["zone"].str.upper() == z]
        if df.empty:
            raise HTTPException(status_code=404, detail=f"no vendors in zone {z}")
    return _records(df)


@app.get("/vendors/{vendor_id}")
def get_vendor(vendor_id: str):
    assert _vendors is not None
    vid = vendor_id.strip()
    row = _vendors[_vendors["vendor_id"].str.upper() == vid.upper()]
    if row.empty:
        raise HTTPException(status_code=404, detail=f"vendor {vid} not found")
    return _records(row)[0]


@app.get("/orders/summary")
def orders_summary():
    assert _orders is not None
    return {
        "order_rows": int(len(_orders)),
        "distinct_vendors": int(_orders["vendor_id"].nunique()),
        "distinct_order_ids": int(_orders["order_id"].nunique()),
        "categories": _orders["category"].value_counts().head(10).astype(int).to_dict(),
    }


@app.get("/orders/by-zone")
def orders_by_zone():
    """Order line counts by stadium zone (join orders → vendors)."""
    return {"zones": _zone_order_counts}
