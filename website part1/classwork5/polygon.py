import turtle
win=turtle.Screen()
win.screensize(400,400)
win.bgcolor('blue')
t= turtle.Turtle()
t.color("black")
n=6
for i in range(n):
    t.forward(100)
    t.right(360/6)

turtle.done()
