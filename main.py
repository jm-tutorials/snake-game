from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen_width = 600
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on = True

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.addPoints()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 288 or abs(snake.head.ycor()) > 288:
        game_is_on = False
        scoreboard.gameOver()

    # Detect collision with tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameOver()

screen.exitonclick()