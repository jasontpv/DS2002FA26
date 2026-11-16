#!/usr/bin/env bash
# Run the PythonAnywhere lesson API on your laptop.
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -d .venv ]]; then
  echo "Creating .venv ..."
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate

PIP_CONFIG_FILE=/dev/null python -m pip install --isolated -q --timeout 60 -r requirements.txt

echo ""
echo "DS2002 PythonAnywhere lesson"
echo "  Docs:   http://127.0.0.1:8000/docs"
echo "  Hello:  http://127.0.0.1:8000/"
echo "  Time:   http://127.0.0.1:8000/time"
echo "  UVA:    http://127.0.0.1:8000/uva"
echo ""
echo "Ctrl+C to stop."
echo ""

exec uvicorn main:app --reload --host 127.0.0.1 --port 8000
