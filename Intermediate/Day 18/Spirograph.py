import random
from turtle import Turtle, Screen

directions = [0, 90, 180, 270]

def random_color():
    r = round(random.randint(0, 255) / 255, 2)
    g = round(random.randint(0, 255) / 255, 2)
    b = round(random.randint(0, 255) / 255, 2)
    color = (r, g, b)
    return color


tim = Turtle()

tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10) 

screen = Screen()
screen.exitonclick()
