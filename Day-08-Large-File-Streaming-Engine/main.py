# Import the streaming reader, log processor, and JSON report writer.
from src.genrator import read_logs
from src.processor import process_log
from src.storage import save_report

# Keep input and output paths relative to the project root.
input_path = "data/sample.log"
output_path = "report.json"

# Read log records lazily, then summarize and save the results.
logs = read_logs(input_path)
summary = process_log(logs)
save_report(output_path, summary)

print("log processing completed successfully!")
print("Report saved to:", output_path)