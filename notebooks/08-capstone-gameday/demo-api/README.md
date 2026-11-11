# Game Day Pulse — FastAPI demo

Small read-only API for in-class demos. Data lives in `../data/` (capstone sample files).

## One command

```bash
./start.sh
```

First run creates `.venv` and installs dependencies. Then open **http://127.0.0.1:8000/docs** in a browser.

## Demo endpoints

| Method | Path | What it returns |
|--------|------|-----------------|
| GET | `/health` | `{ "status": "ok" }` |
| GET | `/vendors` | All vendors (`?zone=A` optional) |
| GET | `/vendors/{vendor_id}` | One vendor, e.g. `V-01` |
| GET | `/orders/summary` | Row counts and top categories |
| GET | `/orders/by-zone` | Order lines per zone A/B/C |

## Try from another terminal

```bash
curl -s http://127.0.0.1:8000/orders/by-zone | python3 -m json.tool
curl -s "http://127.0.0.1:8000/vendors?zone=A" | python3 -m json.tool
```

## Manual setup (same as `start.sh`)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

To let classmates hit your laptop on the same Wi‑Fi, use `--host 0.0.0.0` and share your IP (firewall permitting).
