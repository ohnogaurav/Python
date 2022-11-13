
import turtle
from pygame import mixer
from time import sleep
import sys

#bg music ka bandubass
mixer.init()
mixer.music.load("DEAF KEV - Invincible [NCS Release].mp3")
sleep(1)
mixer.music.play()

#turtle initialization
a=turtle.Turtle()
a.hideturtle()
a.color('blue')
a.speed(1)

#jagah initialization thru out the win
a.width(4)
a.penup()
a.goto(0,-225)
a.pendown()
a.color('black')
a.right(10)

#semi circle
a.begin_fill()
a.circle(100, 180)

#ulta semi circle
a.circle(-100, 180)

#yaha tak 'S' ban chuka hai ab usske circum me circle bana na hai

#circle around 'S' shape
a.circle(-200,180)
a.end_fill()
a.circle(-200,180)

#circle ban jane ke bad andar ka hidden word
a.right(90)
a.penup()
a.forward(100)

#andar wala white circle
a.pendown()
a.color('white')
a.begin_fill()
a.circle(-25)
a.end_fill()

a.penup()
a.forward(200)
a.left(-90)
a.fd(-2)
a.right(90)

#andar wala black circle
a.pendown()
a.color('black')
a.begin_fill()
a.circle(-25)
a.end_fill()

_txt='''
fig :- Yin Yang
'''
for i in _txt:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.1)
sleep(2)
print()
sleep(1)
mixer.music.stop()
