import random
import turtle

t = turtle.Pen()
t.speed(0)
directions = [0, 90, 180, 270]

while True:
    t.setheading(random.choice(directions))
    t.forward(50)
