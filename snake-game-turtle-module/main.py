from turtle import Screen
from data import WIDTH, HEIGHT
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


def create_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def binding_key(screen, snakes):
    screen.listen()
    screen.onkey(fun=snakes.up, key="Up")
    screen.onkey(fun=snakes.down, key="Down")
    screen.onkey(fun=snakes.left, key="Left")
    screen.onkey(fun=snakes.right, key="Right")


screen_window = create_screen()
snake = Snake()
food = Food()
score = ScoreBoard()
binding_key(screen_window, snake)
game_on = True
while game_on:
    screen_window.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    if snake.head.xcor() < -(WIDTH/2 - 20) or snake.head.xcor() > WIDTH/2 - 20 or snake.head.ycor() < -(HEIGHT/2 - 20) or snake.head.ycor() > HEIGHT/2 - 20:
        score.reset()
        snake.reset()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

screen_window.exitonclick()
