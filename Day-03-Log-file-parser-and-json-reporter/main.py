import json

try:
    # Define title banner for CLI telemetry output
    title = "LOG FILE PARSER + JSON REPORTER"
    print(f"\033[1m{'-' * 70}\n{title.center(70)}\n{'-' * 70}\033[0m")

    # Context manager guarantees automatic file descriptor closure upon exit
    with open("app.log", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Initialize severity accumulation counters
    INFO_count = 0
    WARNING_count = 0
    ERROR_count = 0

    # Initialize dynamic payload collection array for extracted anomalies
    error_messages = []

    # Iterate sequentially through stream lines to classify log levels
    for line in lines:
        if "INFO" in line:
            INFO_count += 1
        elif "WARNING" in line:
            WARNING_count += 1
        elif "ERROR" in line:
            ERROR_count += 1
            # Sanitize whitespace and capture critical error payload
            error_messages.append(line.strip())

    # Assemble structured telemetry state dictionary for serialization
    summary = {
       "Total_logs": len(lines),
       "INFO_logs": INFO_count,
       "WARNING_logs": WARNING_count,
       "ERROR_logs": ERROR_count,
       "error_messages": error_messages
    }

    # Serialize aggregated metrics into a persistent, human-readable JSON format
    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print(f"\033[1mJSON REPORTER\033[0m: summary exported to summary.json.")

except FileNotFoundError:
    # Gracefully intercept environmental path faults without crashing the stack trace
    print("Log file not found. Check the file path.")