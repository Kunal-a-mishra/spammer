import pyautogui, time
time.sleep(5)
f = open ("xyz", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")



