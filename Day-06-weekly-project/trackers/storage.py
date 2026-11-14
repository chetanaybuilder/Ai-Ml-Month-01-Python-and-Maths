"""Storage helpers for loading and saving study sessions."""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FILEPATH = BASE_DIR / "data" / "session.json"


def load_sessions():
    """Return all saved sessions or an empty list if no file exists."""
    if not FILEPATH.exists():
        return []

    try:
        with FILEPATH.open("r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return []
            sessions = json.loads(content)
            return sessions if isinstance(sessions, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_sessions(sessions):
    """Store the session list in the JSON database file."""
    FILEPATH.parent.mkdir(parents=True, exist_ok=True)
    with FILEPATH.open("w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=2)

    