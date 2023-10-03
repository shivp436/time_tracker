import pygetwindow as gw
import time
import pyautogui
import re
import pyperclip

def getActiveWindowName():
    activeWindow = gw.getActiveWindow()
    windowName = activeWindow.title.split(" - ")[-1]
    return windowName


def getActiveProjectName():
    activeWindow = gw.getActiveWindow()
    projectName = activeWindow.title.split(" - ")[-2]
    return projectName


def getActiveTabName():
    activeTab = gw.getActiveWindow()
    activeTab.activate()
    time.sleep(0.5)  # Allow some time for the window to activate

    # copy the URL
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('esc')

    # Get the clipboard content
    clipboard_content = pyperclip.paste()

    # Use regex to extract the domain
    match = re.search(r'https?://([A-Za-z_0-9.-]+).*', clipboard_content)
    return match.group(1)