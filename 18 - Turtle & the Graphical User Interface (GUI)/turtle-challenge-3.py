from turtle import Turtle, Screen
import random

# create a Turtle object
timmy = Turtle()
# create a Screen object
screen = Screen()

timmy.speed(2)

colors = ["LightSlateBlue", "DarkRed", "DeepSkyBlue", "LightSeaGreen", "HotPink", "DarkOrchid", "DarkOrange",
          "Gold", "LightPink", "violet"]

# -- DRAW DIFFERENT SHAPES -- #
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shapes_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shapes_side_n)

# exit the screen when the user clicks it
screen.exitonclick()