from turtle import Turtle
import random


class Paddle:
    # def __init__(self, position):
    #     super().__init__()
    #     self.shape("square")
    #     self.shapesize(stretch_len=5)
    #     self.color("white")
    #     self.penup()
    #     self.setheading(90)
    def __init__(self, position, scoreboard_position):
        self.paddle = self.create_paddle(position)
        self.score = 0
        self.scoreboard = Scoreboard(self.score, scoreboard_position)

    @staticmethod
    def create_paddle(position):
        pad = []
        for pos in position:
            new_paddle = Turtle("square")
            new_paddle.penup()
            new_paddle.color("white")
            new_paddle.goto(pos)
            pad.append(new_paddle)
        return pad

    def up(self):
        for pad in self.paddle:
            pad.setheading(90)
            pad.forward(20)

    def down(self):
        for pad in self.paddle:
            pad.setheading(270)
            pad.forward(20)

    def collision(self, ball) -> bool:
        for pad in self.paddle:
            if pad.distance(ball) < 30:
                return True
        return False


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.random_launch()

    def refresh(self):
        self.setposition(0, 0)
        self.random_launch()

    def random_launch(self):
        direction = ["left", "right"]
        rand_dir = random.choice(direction)
        if rand_dir == "left":
            self.setheading(random.randint(120, 240))
        else:
            self.setheading(random.randint(300, 420))

    def move(self):
        self.forward(20)

    def collision_paddle(self):
        self.setheading(180 - self.heading())

    def collision_wall(self):
        self.setheading(360 - self.heading())


class Scoreboard(Turtle):
    def __init__(self, score, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.display_score(score)

    def display_score(self, score):
        self.write(arg=f"{score}", align="center", font=('Arial', 18, 'normal'))
