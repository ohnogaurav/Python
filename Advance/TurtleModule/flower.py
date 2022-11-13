import turtle
a=turtle.Turtle()
s=50
a.speed(0)
for i in range(14):
    a.color('green')
    a.circle(radius=s)
    s+=10
    a.color('red')
    a.circle(radius=s)
    s+=10
s=50
a.right(180)
for j in range(14):
    a.color('green')
    a.circle(radius=s)
    s+=10
    a.color('red')
    a.circle(radius=s)
    s+=10
s=50
a.right(90)
for k in range(20):
    a.color('green')
    a.circle(radius=s)
    s+=10
    a.color('red')
    a.circle(radius=s)
    s+=10
s=50
a.right(180)
for l in range(20):
    a.color('green')
    a.circle(radius=s)
    s+=10
    a.color('red')
    a.circle(radius=s)
    s+=10
