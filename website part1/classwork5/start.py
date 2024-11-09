import turtle
win=turtle.Screen()
win.screensize(400,400)
win.bgcolor('black')
t= turtle.Turtle()
t.color("red")
n=3
for i in range(n):
    t.forward(100)
    t.left(360/3)
t.left(90)
t.penup()
t.forward(70)
t.right(90)
t.pendown()
for i in range(n):
    t.forward(100)
    t.right(360/3)
turtle.done()