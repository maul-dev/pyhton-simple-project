from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.random_direction()
        self.move_distance = 20

    def random_direction(self):
        direction = ["left", "right"]
        rand_dir = random.choice(direction)
        if rand_dir == "left":
            self.setheading(random.randint(120, 240))
        else:
            self.setheading(random.randint(300, 420))

    def move(self):
        self.forward(self.move_distance)

    def bounces_wall(self):
        self.setheading(360 - self.heading())

    def bounces_paddle(self):
        self.setheading(180 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.move_distance = 20
        self.random_direction()

    def increase_speed(self):
        self.move_distance += 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 250)
        self.write(arg=f"{self.l_score}", align="center", font=('Courier', 80, 'normal'))
        self.goto(80, 250)
        self.write(arg=f"{self.r_score}", align="center", font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
