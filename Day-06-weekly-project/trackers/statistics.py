"""Summary calculations for the study tracker application."""

from trackers.storage import load_sessions


def calculate_statistics():
    """Calculate total study time and minutes spent per subject."""
    sessions = load_sessions()
    total_sessions = len(sessions)
    total_minutes = 0
    subject_time = {}

    for session in sessions:
        duration = int(session.get("duration", 0))
        total_minutes += duration

        subject = session.get("subject", "Unknown")
        subject_time[subject] = subject_time.get(subject, 0) + duration

    return {
        "total_sessions": total_sessions,
        "total_minutes": total_minutes,
        "subject_time": subject_time,
    }
