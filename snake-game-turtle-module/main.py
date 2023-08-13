from turtle import Screen
from data import WIDTH, HEIGHT


def create_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("black")
    screen.tracer(0)
    return screen


screen_window = create_screen()

screen_window.update()
screen_window.exitonclick()
