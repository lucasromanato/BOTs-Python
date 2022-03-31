from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Title 1 Position: X:  333 Y:  509 RGB: (174, 132,  73)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001) #isso pausa por 0.0001 segundos
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(333, 509):
        click(333, 509)
    
