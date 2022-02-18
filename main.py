from turtle import Screen
from snake import Snake
from Food import food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
position = [0, -20, -40]
screen.tracer(0)

snake = Snake()
food = food()
scores = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
end_game = False

while not end_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision from food
    if snake.head.distance(food) < 15:
        food.food_location()
        snake.extend()
        scores.increase_score()

    # Detect Collision from food
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        end_game = True
        scores.game_over()

    # Detect Snake Collision with tail
    for segment in snake.snakes[1:]:
        
        if snake.head.distance(segment) < 10:
            end_game = True
            scores.game_over()

screen.exitonclick()
