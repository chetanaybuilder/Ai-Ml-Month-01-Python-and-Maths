# Summarize total records and supported severity levels.


def process_log(logs):
    total_count = 0
    info_count = 0
    warning_count = 0
    error_count = 0

    # Ignore metadata lines so they do not affect record counts.
    for log in logs:
        if not log or log.startswith("#"):
            continue

        total_count += 1
        fields = log.split()
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

    summary = {
        "total": total_count,
        "info": info_count,
        "warning": warning_count,
        "error": error_count
    }
    return summary
