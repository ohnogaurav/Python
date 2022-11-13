import pyautogui as a
a.moveTo(448,459)
a.dragTo(515,525,button='right')
a.click()
a.moveTo(77,438)
a.keyDown('fn')
for i in range(50):
    a.hotkey('f5')
a.keyUp('fn')
