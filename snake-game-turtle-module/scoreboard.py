from turtle import Turtle
from data import HEIGHT,ALIGN,FONT


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=HEIGHT/2 - 30)
        self.display_score()

    def update_score(self):
        self.clear()
        self.score +=1
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)