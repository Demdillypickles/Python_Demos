import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(100)

# Here is where we ask for a number


#sides = int(input("How many colors would you like(1-6)?>>>"))

sides = int(turtle.numinput("Color Spiral", "How many colors would you like?", 3, 1, 6))


colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides // 200)
