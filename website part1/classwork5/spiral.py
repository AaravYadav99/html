import turtle
win=turtle.Screen()
win.title("spiral")
win.bgcolor('black')
t=turtle.Turtle()
t.color("gold")
for i in range(100):
    t.forward(i*3)
    t.left(90)
turtle.done()