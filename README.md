# CtrlAwake

Utility to prevent Linux systems from going idle.
Mouse jiggle + power inhibit + tray app.

## Features
- Random mouse movement
- Prevent sleep
- Prevent screen lock
- System tray control
- Configurable intervals
- Launch at login

## Dev Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
