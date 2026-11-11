#!/usr/bin/env bash
# Start the Game Day Pulse demo API (creates .venv on first run).
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -d .venv ]]; then
  echo "Creating .venv ..."
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

# PIP_CONFIG_FILE=/dev/null ignores ~/.config/pip/pip.conf (extra index can hang).
PIP_CONFIG_FILE=/dev/null python -m pip install --isolated -q --timeout 60 -r requirements.txt

echo ""
echo "Game Day Pulse API"
echo "  Swagger UI:  http://127.0.0.1:8000/docs"
echo "  Health:      http://127.0.0.1:8000/health"
echo "  Vendors:     http://127.0.0.1:8000/vendors"
echo "  By zone:     http://127.0.0.1:8000/orders/by-zone"
echo ""
echo "Ctrl+C to stop."
echo ""

exec uvicorn main:app --reload --host 127.0.0.1 --port 8000
