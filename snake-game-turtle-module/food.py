from turtle import Turtle
from random import randint
from data import WIDTH, HEIGHT


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = randint(-(WIDTH/2 - 20), WIDTH/2 - 20)
        rand_y = randint(-(HEIGHT/2 - 20), HEIGHT / 2 - 20)
        self.goto(rand_x, rand_y)


