from turtle import Screen
from paddle import Paddle, Ball
import time


def create_screen():
    screen = Screen()
    screen.setup(width=1280, height=720)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def binding_key(screen, f_paddle, s_paddle):
    screen.listen()
    screen.onkeypress(fun=f_paddle.up, key="Up")
    screen.onkeypress(fun=f_paddle.down, key="Down")
    screen.onkeypress(fun=s_paddle.up, key="w")
    screen.onkeypress(fun=s_paddle.down, key="s")


first_paddle_position = (-600, 0)
second_paddle_position = (600, 0)

screen_window = create_screen()
first_paddle = Paddle(first_paddle_position)
second_paddle = Paddle(second_paddle_position)
ball = Ball()
binding_key(screen_window, first_paddle, second_paddle)

game_is_on = True
while game_is_on:
    screen_window.update()
    time.sleep(0.1)
    ball.move()
    if first_paddle.distance(ball) < 30 or second_paddle.distance(ball) < 30:
        ball.collision_paddle()
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.collision_wall()

screen_window.exitonclick()
