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


first_paddle_position = [(-600, 0), (-600, 20), (-600, 40), (-600, -20), (-600, -40)]
second_paddle_position = [(600, 0), (600, 20), (600, 40), (600, -20), (600, -40)]

screen_window = create_screen()
first_paddle = Paddle(first_paddle_position, (-60, 300))
second_paddle = Paddle(second_paddle_position, (60, 300))
ball = Ball()
binding_key(screen_window, first_paddle, second_paddle)

game_is_on = True
while game_is_on:
    screen_window.update()
    time.sleep(0.1)
    ball.move()
    if first_paddle.collision(ball) or second_paddle.collision(ball):
        ball.collision_paddle()

    if ball.ycor() > 345 or ball.ycor() < -345:
        ball.collision_wall()

    if ball.xcor() > 1280/2 or ball.xcor() < -1280/2:
        first_paddle.score +=1
        ball.refresh()

screen_window.exitonclick()
