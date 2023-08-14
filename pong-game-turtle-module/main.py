from turtle import Screen
from paddle import Paddle
import time


def create_screen():
    screen = Screen()
    screen.setup(width=1280, height=720)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def binding_key(screen):
    screen.listen()
    screen.onkeypress(fun=first_paddle.up, key="Up")
    screen.onkeypress(fun=first_paddle.down, key="Down")
    screen.onkeypress(fun=second_paddle.up, key="w")
    screen.onkeypress(fun=second_paddle.down, key="s")


first_paddle_position = [(-600, 0), (-600, 20), (-600, -20)]
second_paddle_position = [(600, 0), (600, 20), (600, -20)]

screen_window = create_screen()
first_paddle = Paddle(first_paddle_position)
second_paddle = Paddle(second_paddle_position)
binding_key(screen_window)

game_is_on = True
while game_is_on:
    screen_window.update()
    time.sleep(0.1)

screen_window.exitonclick()
