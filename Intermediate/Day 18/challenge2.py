import random
from turtle import Turtle, Screen

directions = [0, 90, 180, 270]

def random_color():
    r = round(random.randint(0, 255) / 255, 2)
    g = round(random.randint(0, 255) / 255, 2)
    b = round(random.randint(0, 255) / 255, 2)
    color = (r, g, b)
    return color

def random_direction():
    direction = random.choice(directions)
    lr = random.choice(["left", "right"]) 
    return f"tim.{lr}({direction})"

def random_length():
    length = random.randint(50, 100)
    return f"tim.forward({length})"

tim = Turtle()
tim.width(3)
tim.shape("turtle")
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    eval(random_length())
    eval(random_direction())

screen = Screen()
screen.exitonclick()
