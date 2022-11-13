
#use this only if your program does not need python console to excute

import pyautogui as a

c=a.password(text='This file is protected plz enter your password',title='User varification ☺',mask='*')

#content will be displayed if password is correct
if c=='put_your_password_here':
    print('opening program ☺')
    #put your code block here


else:
    print()#donothing
