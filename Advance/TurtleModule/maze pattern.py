import turtle

a=turtle.Turtle()
a.hideturtle()

s=10
for i in range (25):
    a.shape('triangle')
    a.speed(0)
    a.forward(s)
    a.right(90)
    a.forward(s)
    a.right(90)
    s+=10
    a.forward(s)
    a.right(90)
    a.forward(s)
    a.right(90)
    s+=10


turtle.mainloop()
