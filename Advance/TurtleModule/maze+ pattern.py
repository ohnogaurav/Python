import turtle

a=turtle.Turtle()

s=10
for i in range (50):
    a.speed(0)
    a.forward(s)
    a.right(90)
    a.forward(s)
    a.right(90)
    s+=10
    a.forward(s)
    a.right(90)
    a.forward(s)
turtle.mainloop()
