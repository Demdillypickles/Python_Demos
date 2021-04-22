from random import sample, choice
import turtle

t = turtle.Pen()
t.speed(0)
directions = [0, 90, 180, 270]
colors = ["red", "yellow", "blue", "orange", "green", "purple"]

size = turtle.screensize()
t.width(5)


def reset():
    next_colors = sample(colors, 2)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pencolor(next_colors[0])
    turtle.bgcolor(next_colors[1])


def check_boundary():
    xpos = size[0]
    ypos = size[1]
    xneg, yneg = -xpos, -ypos

    if xneg > t.xcor():
        reset()
    if t.xcor() > xpos:
        reset()
    if yneg > t.ycor():
        reset()
    if t.ycor() > ypos:
        reset()


while True:
    t.setheading(choice(directions))
    t.forward(25)
    check_boundary()
