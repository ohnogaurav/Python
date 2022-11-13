import pyautogui as a
import keyboard
import random
keyboard.wait('s')
while keyboard.is_pressed("q") == False:
    try:
        if a.pixel(1296,380)[0] == 172 :
            a.hotkey('space')
            print('jumped !')
            count+=1
    except:
        print('running....')
#tile 1 position X: 1291 Y:  382 RGB: ( 32,  33,  36)
#for checking RGB X: 1184 Y:  344 RGB: (172, 172, 172)
