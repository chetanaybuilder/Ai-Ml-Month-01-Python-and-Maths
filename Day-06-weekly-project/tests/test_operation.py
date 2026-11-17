"""Tests for the study tracker operations.

These test cases verify that session records are saved correctly,
retrieved successfully, and summarized as expected.
"""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from trackers.operation import add_session, view_sessions
from trackers.statistics import calculate_statistics


class TestStudyTracker(unittest.TestCase):
    """Check the main functions used to manage study sessions."""

    def test_add_session(self):
        """A new session should be stored with all provided details."""
        with tempfile.NamedTemporaryFile("w+", delete=False) as temp:
            temp.write("[]")
            temp_path = Path(temp.name)

        with patch("trackers.storage.FILEPATH", temp_path):
            session = add_session("Math", "2026-11-14", 45, "Algebra")

        self.assertEqual(session["subject"], "Math")
        data = json.loads(temp_path.read_text())
        self.assertEqual(len(data), 1)
        temp_path.unlink()

    def test_view_sessions(self):
        """Saved sessions should be returned from storage as a list."""
        with tempfile.NamedTemporaryFile("w+", delete=False) as temp:
            json.dump([
                {"subject": "Science", "date": "2026-11-14", "duration": 30, "chapter": "Physics"}
            ], temp)
            temp_path = Path(temp.name)

        with patch("trackers.storage.FILEPATH", temp_path):
            sessions = view_sessions()

        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0]["subject"], "Science")
        temp_path.unlink()

    def test_statistics(self):
        """Statistics should total all minutes and group them by subject."""
        with tempfile.NamedTemporaryFile("w+", delete=False) as temp:
            json.dump([
                {"subject": "Math", "date": "2026-11-14", "duration": 20, "chapter": "Algebra"},
                {"subject": "Math", "date": "2026-11-15", "duration": 30, "chapter": "Geometry"},
                {"subject": "Science", "date": "2026-11-16", "duration": 40, "chapter": "Physics"}
            ], temp)
            temp_path = Path(temp.name)

        with patch("trackers.storage.FILEPATH", temp_path):
            stats = calculate_statistics()

        self.assertEqual(stats["total_sessions"], 3)
        self.assertEqual(stats["total_minutes"], 90)
        self.assertEqual(stats["subject_time"]["Math"], 50)
        temp_path.unlink()


if __name__ == "__main__":
    unittest.main()
