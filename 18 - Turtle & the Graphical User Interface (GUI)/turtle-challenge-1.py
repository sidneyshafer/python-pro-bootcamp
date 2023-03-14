# -- WAYS TO IMPORT MODULES AND PACKAGES -- #
# Basic Import -->     import turtle
#                   (keyword) (Module name)

# from...import... --> from     turtle      import      Turtle,        Screen
#                 (Keyword)  (Module name) (Keyword) (Thing in module) (another thing in module)

# from..import.. --> from       turtle      import      *   <-- NOT A GOOD IDEA!!
#                 (keyword) (module name) (keyword) (everything)

# Aliasing Modules -->  import      turtle      as      t
#                   (keyword)  (module name) (keyword) (alias name)
# alias example: tim = t.Turtle()

# Installing Modules: pypi.org --> example:: import heroes (must install module)

# import Turtle() and Screen() class from turtle module
from turtle import Turtle, Screen

# turtle graphics documentation: https://docs.python.org/3/library/turtle.html
# turtle graphics colors: https://cs111.wellesley.edu/reference/colors

# create a Turtle object
timmy = Turtle()
# create a Screen object
screen = Screen()
# set the turtle shape using the shape() method
timmy.shape("turtle")
# change the turtle color
timmy.color("MediumOrchid")

# -- DRAW A SQUARE -- #
for _ in range(4):
    # move timmy forward 100 paces
    timmy.forward(100)
    # turn timmy to the right by 90 deg
    timmy.right(90)


# exit the screen when the user clicks it
screen.exitonclick()