#!/usr/bin/env sh
trap 'kill $(jobs -p)' EXIT

ngrok http $1 > /dev/null &
python ngrok_deploy.py
uvicorn bot:app --port $1