from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import ScoreBoard

from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.snake_move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
