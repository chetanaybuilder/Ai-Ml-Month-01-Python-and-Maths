# Create a summary of log records by severity level.
def process_log(logs):
    """Count log records and categorize supported severity levels."""
    total_count = 0
    info_count = 0
    warning_count = 0
    error_count = 0

    # Process the iterable one record at a time to keep memory usage low.
    for log in logs:
        if not log or log.startswith("#"):
            continue

        total_count += 1
        fields = log.split()

        # Severity may follow a date and time, so inspect the first three fields.
        level = next(
            (field for field in fields[:3] if field in {"INFO", "WARNING", "ERROR"}),
            "",
        )

        if level == "INFO":
            info_count += 1
        elif level == "WARNING":
            warning_count += 1
        elif level == "ERROR":
            error_count += 1

    # Return counts in the shape expected by the JSON report writer.
    summary = {
        "total": total_count,
        "info": info_count,
        "warning": warning_count,
        "error": error_count
    }
    return summary
