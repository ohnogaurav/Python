import turtle
t=1
for x in range (4):
    turtle.speed(1)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.pencolor('blue')
    turtle.forward(100)
    t+=1
turtle.right(90)
turtle.pencolor('black')
turtle.forward(200)
turtle.backward(100)
turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.pencolor('black')
turtle.backward(200)
'''for x in range (100):
    turtle.forward(30)
    turtle.right(30)'''
