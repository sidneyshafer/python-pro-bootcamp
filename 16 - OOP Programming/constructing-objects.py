# Attributes:
    # variables, describe class/object
    # Modeled by variables
    # what it "has"
# Methods:
    # Functions; what a modeled object can do
    # Modeled by functions
    # what it "does"

# Example: car = CarBlueprint()
    # car -> Object
    # CarBlueprint() -> Class

from turtle import Turtle, Screen
# Creating an object from the turtle module
timmy = Turtle()
print(timmy)
# Change shape
timmy.shape("turtle")
# Change color
timmy.color("coral")
# Move forward by 100 paces
timmy.forward(100)

# Object Attributes: car.speed -> object.attribute

my_screen = Screen()
print(my_screen.canvheight)

# Method: car.stop() -> object.method()
my_screen.exitonclick()