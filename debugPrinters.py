from helpers import getCrDate, getCrTime, formatProjectName
from snippets import getActiveWindowName, getActiveProjectName, getActiveTabName

def recordNewInstance(activeWindow, activeTime, startTime):
    print(f"Recorded New Instance: {activeWindow} - Duration: {activeTime} - Start: {startTime} - Time: {getCrTime()}")

def insertNewInstance(activeWindow, activeTime, startTime):
    if(activeWindow == "Visual Studio Code"):
        subWindow = formatProjectName(getActiveProjectName())
    elif(activeWindow == "Google Chrome"):
        subWindow = getActiveTabName()
    else:
        subWindow = None
    print(f"Inserted New Instance: {activeWindow}-{subWindow} - Duration: {activeTime} - Start: {startTime} - Time: {getCrTime()}")

def updateInstance(activeWindow, activeTime):
    print(f"Updated New Instance: {activeWindow} - Duration: {activeTime} - Time: {getCrTime()}")
        