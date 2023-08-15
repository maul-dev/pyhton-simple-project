from turtle import Screen
from paddle import Paddle, Ball, Scoreboard
import time


def create_screen():
    screen = Screen()
    screen.setup(width=1280, height=720)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


def binding_key(screen, f_paddle, s_paddle):
    screen.listen()
    screen.onkeypress(fun=f_paddle.up, key="w")
    screen.onkeypress(fun=f_paddle.down, key="s")
    screen.onkeypress(fun=s_paddle.up, key="Up")
    screen.onkeypress(fun=s_paddle.down, key="Down")


l_paddle_position = (-600, 0)
r_paddle_position = (600, 0)

screen_window = create_screen()
l_paddle = Paddle(l_paddle_position)
r_paddle = Paddle(r_paddle_position)
ball = Ball()
score = Scoreboard()
binding_key(screen_window, l_paddle, r_paddle)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen_window.update()
    ball.move()
    if (ball.distance(l_paddle) < 50 and abs(ball.xcor() - l_paddle.xcor()) < 30) or \
            (ball.distance(r_paddle) < 50 and abs(ball.xcor() - r_paddle.xcor()) < 30):
        ball.bounces_paddle()
        ball.increase_speed()

    if ball.ycor() > 345 or ball.ycor() < -345:
        ball.bounces_wall()

    if ball.xcor() > 650:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -650:
        ball.reset_position()
        score.r_point()

screen_window.exitonclick()
