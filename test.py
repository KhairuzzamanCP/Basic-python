import pyautogui
import time
n = int(input())
time.sleep(5)

for i in range(1,n+1):
    string = "#" * i
    pyautogui.typewrite(string)
    pyautogui.press('enter')
    print(string)





