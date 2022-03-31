from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# X:  759 Y:  245 RGB: (172, 172, 172)

def click(x, y):
       win32api.SetCursorPos((x,y))
       win32api.keybd_event(0X20, 0, 0, 0)
       time.sleep(0.05)
       win32api.keybd_event(0X20, 0, win32con.KEYEVENTF_KEYUP, 0)

while keyboard.is_pressed('q') == False:

       if pyautogui.pixel(770, 255)[0] == 172:
              click(770, 255)
