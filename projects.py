from snippets import getActiveWindowName
from helpers import getCrTime
from jsonMethods import insertApp, updateApp
import time

def main():
    prevWindow= None
    sleepTime: int = 1 # 1 minute
    activeDurn: int = 0
    minDuration: int = 1 # 1 minute
    startTime: str = None

    while True:
        activeWindow = getActiveWindowName()

        if activeWindow != "": # if active window is not empty
            if(activeWindow == prevWindow):
                activeDurn += sleepTime

            if(activeWindow != prevWindow):
                prevWindow = activeWindow # update prevWindow
                activeDurn = 0 # reset activeDurn
                startTime = getCrTime() # get startTime

            if activeDurn == minDuration:
                insertApp(activeWindow, activeDurn, startTime)

            if activeDurn > minDuration:
                updateApp(activeDurn)
        else:
            activeDurn = 0
            prevWindow = None

        time.sleep(sleepTime)

if __name__ == "__main__":
    main()