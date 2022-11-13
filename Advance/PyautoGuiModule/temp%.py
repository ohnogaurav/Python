import pyautogui as a
from time import sleep


a.hotkey('winleft')
a.typewrite('%temp%\n',0.2)
#sleep(1)
a.hotkey('ctrl','a')
a.hotkey('shift','del')
a.hotkey('enter')
