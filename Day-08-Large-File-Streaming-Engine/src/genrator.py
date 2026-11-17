#importing required library
import os


#Log file location
filepath = "data/sample.log"


#creating a generator function so it can read log file line by line
def read_logs(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("Log file not found!")
    with open(filepath, "r", encoding="utf-8") as file:
          for line in file:
            yield line.strip()
