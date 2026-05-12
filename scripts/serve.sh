#!/bin/bash
# Rebuild + restart dev server.  Works around mkdocs serve sometimes
# serving stale CSS/JS after file changes.
set -e
cd "$(dirname "$0")/.."
pkill -f "mkdocs serve" 2>/dev/null || true
sleep 1
.venv/bin/python -m mkdocs build
echo ""
echo "  ✔  Site rebuilt"
echo "  ✔  Dev server at http://127.0.0.1:8000/hi3403-docs/"
echo ""
exec .venv/bin/python -m mkdocs serve
