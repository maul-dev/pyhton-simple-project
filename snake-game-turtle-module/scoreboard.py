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
        self.score += 1
        self.display_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
        self.goto(0, -30)
        self.write(arg=f"Total Score: {self.score}", align=ALIGN, font=FONT)

    def display_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)
