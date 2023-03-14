# This Snake Game is a builds off of the snake game
# in section 20 and keeps track of high score

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
# Turn screen tracer off --> does not run code until 'update' is called
screen.tracer(0)

# Create a new Snake object from the snake class
snake = Snake()
# Create new food object
food = Food()
# Create scoreboard object
scoreboard = Scoreboard()

# Use listen() method of screen class to listen to keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:

    # update the screen every 0.1 second
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()
