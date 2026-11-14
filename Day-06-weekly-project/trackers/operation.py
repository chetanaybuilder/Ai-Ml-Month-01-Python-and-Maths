"""Operations for adding and retrieving study sessions."""

from trackers.storage import load_sessions, save_sessions


def add_session(subject, date, duration, chapter):
    """Add a study session to storage and return the saved record."""
    sessions = load_sessions()

    session = {
        "subject": subject,
        "date": date,
        "duration": int(duration),
        "chapter": chapter,
    }

    sessions.append(session)
    save_sessions(sessions)
    return session


def view_sessions():
    """Return all saved sessions from storage."""
    return load_sessions()
