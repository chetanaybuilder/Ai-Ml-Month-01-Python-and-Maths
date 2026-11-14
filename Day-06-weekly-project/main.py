"""Study tracker entry point with a user-friendly terminal interface."""

from trackers.operation import add_session, view_sessions
from trackers.statistics import calculate_statistics

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"


def colorize(text, color):
    """Apply a color to a string for the terminal."""
    return f"{color}{text}{RESET}"


def print_section(title):
    """Display a neat section heading in the console."""
    border = "=" * 60
    print("\n" + colorize(border, CYAN))
    print(colorize(title.center(60), BOLD + CYAN))
    print(colorize(border, CYAN))


def show_menu():
    """Render the main menu in a clear, decorated layout."""
    print_section("STUDY TRACKER")
    print(colorize("1. Add session", GREEN))
    print(colorize("2. View sessions", GREEN))
    print(colorize("3. View statistics", GREEN))
    print(colorize("4. Exit", RED))
    print(colorize("-" * 60, YELLOW))


def show_sessions():
    """Print all saved sessions in a friendly format."""
    sessions = view_sessions()
    if not sessions:
        print(colorize("No sessions found yet.", YELLOW))
        return

    print_section("SAVED STUDY SESSIONS")
    for index, session in enumerate(sessions, start=1):
        print(
            f"{index}. Subject: {session.get('subject', 'N/A')} | "
            f"Chapter: {session.get('chapter', 'N/A')} | "
            f"Date: {session.get('date', 'N/A')} | "
            f"Duration: {session.get('duration', 0)} minutes"
        )


def show_statistics():
    """Display summary statistics for all learning sessions."""
    stats = calculate_statistics()
    print_section("STUDY STATISTICS")
    print(f"Total sessions: {stats['total_sessions']}")
    print(f"Total minutes: {stats['total_minutes']}")

    if stats['subject_time']:
        print("\nMinutes per subject:")
        for subject, minutes in stats['subject_time'].items():
            print(f"- {subject}: {minutes} minutes")
    else:
        print(colorize("No study statistics available yet.", YELLOW))


def main():
    """Run the interactive tracker until the user exits."""
    while True:
        show_menu()
        choice = input(colorize("Enter your choice: ", BOLD)).strip()

        if choice == "1":
            print_section("ADD SESSION")
            subject = input("Enter subject: ").strip()
            chapter = input("Enter chapter: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            duration = input("Enter duration in minutes: ").strip()

            try:
                duration_value = int(duration)
            except ValueError:
                print(colorize("Duration must be a valid number.", RED))
                continue

            if not subject or not chapter or not date:
                print(colorize("Subject, chapter, and date are required.", RED))
                continue

            add_session(subject, date, duration_value, chapter)
            print(colorize("Session added successfully!", GREEN))

        elif choice == "2":
            show_sessions()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            print_section("GOODBYE")
            print(colorize("Thank you for studying with us!", GREEN))
            break

        else:
            print(colorize("Invalid choice. Please select a valid option.", RED))


if __name__ == "__main__":
    main()

 