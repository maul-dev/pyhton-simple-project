from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="Center", font=FONT)