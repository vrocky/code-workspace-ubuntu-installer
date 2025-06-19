import json
import os
from pathlib import Path

STATE_PATH = Path.home() / '.installer-state' / 'install_status.json'

def load_state():
    if STATE_PATH.exists():
        with STATE_PATH.open() as f:
            return json.load(f)
    return {}

def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open('w') as f:
        json.dump(state, f, indent=2)
