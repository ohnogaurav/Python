from pygame import mixer
import turtle
import time
from time import sleep
mixer.init()
mixer.music.load('JPB - Up.mp3')
mixer.music.play()
a=turtle.Turtle()

a.width(3)


def ghr():
    a.penup()
    a.home()
    a.pendown()
sleep(1)
a.color('lightgreen')
a.begin_fill()
a.circle(200,90)
ghr()
a.left(90)
a.circle(-200,90)
a.end_fill()

ghr()
a.left(90)
a.begin_fill()
a.circle(200,90)

ghr()
a.right(180)
a.circle(-200,90)
a.end_fill()



ghr()
a.right(90)
a.begin_fill()
a.circle(200,90)

ghr()
a.circle(-200,90)
a.end_fill()


ghr()
a.right(90)
a.begin_fill()
a.circle(-200,90)

ghr()
a.right(180)
a.circle(200,90)
a.end_fill()


ghr()

a.penup()
a.goto(0,75)
a.pendown()

a.color('light blue')
a.begin_fill()
a.circle(20)
a.end_fill()

a.left(90)
a.penup()
a.forward(40)
a.pendown()

a.width(5)
a.circle(100,90)
a.circle(5)
a.right(180)
a.penup()
a.circle(-100,90)
a.pendown()

a.right(180)
a.circle(-100,90)
a.circle(-5)
a.width(3)
a.hideturtle()


sleep(10)
mixer.music.stop()







