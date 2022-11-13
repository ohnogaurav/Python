from pyautogui import *
import pyautogui as a
import time
import keyboard
import random
import win32api, win32con

#tile 1 position X: 1340 Y:  671 RGB: (151, 202, 255)
#tile 2 position X: 1492 Y:  671 RGB: (157, 215, 255)
#tile 3 position X: 1628 Y:  671 RGB: ( 54, 159, 198)
#tile 4 position X: 1776 Y:  671 RGB: (157, 188, 250)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    try:

        if a.pixel(1340,720)[0] == 0 :
            click(1340,720)
        if a.pixel(1492,720)[0] == 0 :
            click(1492,720)
        if a.pixel(1628,720)[0] == 0 :
            click(1628,720)
        if a.pixel(1776,720)[0] == 0 :
            click(1776,720)
    except:
        print('handling exceptions background , enjoy your foreground:)')

