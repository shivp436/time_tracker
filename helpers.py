from datetime import datetime
import os
import json

def getCrDate():
    return datetime.now().date().strftime("%Y-%m-%d")

def getCrTime():
    return datetime.now().time().strftime("%H:%M:%S")

def formatProjectName(s):
    formattedName = s.strip().replace("_", " ").title()
    return formattedName

def fetchJsondata():
    records = []
    try:
        with open(f"records/{getCrDate()}.json", "r") as f:
            if os.stat(f"records/{getCrDate()}.json").st_size > 0:
                records = json.load(f)
            else:
                print("File is empty. Adding data now")
    except FileNotFoundError as f:
        print(f"File not found. Creating & adding data")
    return records

def updateJsonData(records):
    try:
        with open(f"records/{getCrDate()}.json", "w") as f:
            json.dump(records, f, indent=4)
    except Exception as e:
        print(f"Error: Could not write to file {e}")
