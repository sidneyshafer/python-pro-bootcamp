import turtle
from turtle import Turtle, Screen
import random

# create a Turtle object
timmy = Turtle()
# create a Screen object
screen = Screen()
# change color mode
turtle.colormode(255)

# colors = ["LightSlateBlue", "DarkRed", "DeepSkyBlue", "LightSeaGreen", "HotPink", "DarkOrchid", "DarkOrange",
# "Gold", "LightPink", "violet"]


def random_color():
    # generate a random red color value
    r = random.randint(0, 255)
    # generate a random green color value
    g = random.randint(0, 255)
    # generate a random blue color value
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

# -- GENERATE A RANDOM WALK -- #
for _ in range(200):
    # timmy.color(random.choice(colors))
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


# exit the screen when the user clicks it
screen.exitonclick()

# Tuples:
# - cannot change tuples or remove items
# - they are 'set and stone'
# - are 'Immutable' --> lists ARE immutables (can change and edit them)
# can change tuple by converting it to a list like this: list(tuple_name)