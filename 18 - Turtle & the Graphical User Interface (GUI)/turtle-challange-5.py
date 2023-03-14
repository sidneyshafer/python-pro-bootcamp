import turtle
from turtle import Turtle, Screen
import random

# create a Turtle object
timmy = Turtle()
# create a Screen object
screen = Screen()
# set color mode
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        # draw a circle by passing in the radius
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(3)

# exit the screen when the user clicks it
screen.exitonclick()