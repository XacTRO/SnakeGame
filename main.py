from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left_, "Left")
screen.onkey(snake.right_, "Right")

screen.update()
game_is_on = True

while game_is_on:
    score.writing_score()
    screen.update()
    time.sleep(0.15)
    snake.move()

    score.writing_score()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        score.score += 1
        food.refresh()
        snake.extend()
        score.clear()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()