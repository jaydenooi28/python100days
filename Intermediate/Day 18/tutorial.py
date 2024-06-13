from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")




# TODO draw a square

# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)


# TODO dotted line
for _ in range(15):
    timmy.fd(10)
    timmy.penup()
    timmy.fd(10)
    timmy.pendown()




screen = Screen()
screen.exitonclick()
