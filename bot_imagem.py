from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Title 1 Position: X:  597 Y:  471 RGB: (  0,   0,   0)
#Title 2 Position: X:  710 Y:  471 RGB: (255, 255, 255)
#Title 3 Position: X:  805 Y:  471 RGB: (255, 255, 255)
#Title 4 Position: X:  900 Y:  471 RGB: (178, 182, 234)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #isso pausa por 0.01 segundos
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(597, 471)[0] == 0:
        click(597, 471)
    if pyautogui.pixel(710, 471)[0] == 0:
        click(710, 471)
    if pyautogui.pixel(805, 471)[0] == 0:
        click(805, 471)
    if pyautogui.pixel(900, 471)[0] == 0:
        click(900, 471)
