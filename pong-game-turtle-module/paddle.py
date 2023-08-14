from turtle import Turtle
from random import randint


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.setposition(position)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.setheading(randint(0, 360))

    def move(self):
        self.forward(20)

    def collision_paddle(self):
        self.setheading(180 - self.heading())

    def collision_wall(self):
        self.setheading(360 - self.heading())
