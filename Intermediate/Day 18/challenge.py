import random
from turtle import Turtle, Screen

def random_color():
    r = round(random.randint(0, 255) / 255, 2)
    g = round(random.randint(0, 255) / 255, 2)
    b = round(random.randint(0, 255) / 255, 2)
    color = (r, g, b)
    return color

def calculate_angle(x):
    ans = 360 / x
    return int(ans)

my_turtle = Turtle()

x = 3
while x < 9:
    my_turtle.pencolor(random_color())
    result = calculate_angle(x)
    for _ in range(x):
        my_turtle.right(result)
        my_turtle.forward(100)
    x += 1

screen = Screen()
screen.exitonclick()
