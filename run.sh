#!/bin/bash

PORT=${1:-8000}

echo "Starting local server at http://localhost:$PORT"
echo "Press Ctrl+C to stop"
echo ""

python3 -m http.server $PORT
