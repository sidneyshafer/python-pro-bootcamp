import turtle
from turtle import Turtle, Screen
import colorgram
import random

# create a Turtle object
t = Turtle()
# remove pen
t.penup()
# hide the turtle
t.hideturtle()
# create a Screen object
screen = Screen()
# set color mode
turtle.colormode(255)
# set speed
t.speed("fastest")

# rgb_colors = []
# colors = colorgram.extract('SpotPainting.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


color_list = [(230, 215, 101), (154, 80, 38), (244, 231, 236), (207, 159, 105),
 (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
 (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169),
 (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46),
 (132, 79, 90), (18, 75, 105)]

# set heading
t.setheading(225)
t.forward(250)
t.setheading(0)
num_of_dots = 100

# draw a dot by passing in the size and color
# must set colormode to rgb
for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


# exit the screen when the user clicks it
screen.exitonclick()