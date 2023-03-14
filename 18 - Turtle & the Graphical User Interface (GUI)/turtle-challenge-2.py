from turtle import Turtle, Screen

# create a Turtle object
timmy = Turtle()
# create a Screen object
screen = Screen()

# -- DRAW A DASHED LINE -- #

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# exit the screen when the user clicks it
screen.exitonclick()