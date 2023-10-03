from helpers import getCrDate, getCrTime, formatProjectName, fetchJsondata, updateJsonData

def insertApp(activeWindow, duration, startTime):
    records = fetchJsondata()

    newRecord = {
        "window": activeWindow,
        "startTime": startTime,
        "durn": duration,
        "endTime": getCrTime(),
    }
    records.append(newRecord)

    updateJsonData(records)

def updateApp(duration):
    # TODO: update the last window duration and end time
    records = fetchJsondata()
    records[-1]["durn"] = duration
    records[-1]["endTime"] = getCrTime()
    updateJsonData(records)