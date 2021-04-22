import turtle


def next_value(current: int, step: int):
    """
    This is a function that endlessly counts up and down between 0 and 255.
    You can control the size of the steps with 'step'
    """
    # Do this forever
    while True:
        # get the next value by adding the step to the current value
        value = current + step
        # check if the value has crossed one of the boundaries
        if value > 255:
            # wrap around: 254 + 2 = 254 | 254 + 4 = 251 | 253 + 7 = 250
            value = value - (value - 255) * 2
            # flip the sign of 'step' to reverse the counting direction
            step = - step

        elif value < 0:
            value = abs(value)
            step = - step

        current = value
        yield value


t = turtle.Pen()
turtle.bgcolor('black')
t.speed(100)
turtle.colormode(255)

# -----------------------------\
# Try changing these values!

sides = 7
red = next_value(64, 30)
green = next_value(192, 7)
blue = next_value(128, 7)

# -----------------------------/

for x in range(360):
    t.pencolor(next(red), next(blue), next(green))
    t.forward(x * 2 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides // 200)



