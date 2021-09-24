import pyautogui
import time
from datetime import datetime

Time1 = "15:36:50"
Time2 = "15:36:53"
t = 0
while t < 2:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    if current_time == Time1:
        screenshot = pyautogui.screenshot()
        screenshot.save("FirstPicAt_" + Time1.replace(":", "") + ".png")
        t += 1
    elif current_time == Time2:
        screenshot = pyautogui.screenshot()
        screenshot.save("SecondPicAt_" + Time2.replace(":", "") + ".png")
        t += 1
    time.sleep(1)
