#importing required module
import json


#creating a function save data in json form
def save_report(filepath,summary):

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
