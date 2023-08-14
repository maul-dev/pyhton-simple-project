from turtle import Turtle


class Paddle:
    def __init__(self, position):
        self.paddle = self.create_paddle(position)

    @staticmethod
    def create_paddle(position):
        paddle = []
        for pos in position:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(pos)
            paddle.append(new_square)
        return paddle

    def up(self):
        for pad in self.paddle:
            pad.setheading(90)
            pad.forward(50)

    def down(self):
        for pad in self.paddle:
            pad.setheading(270)
            pad.forward(50)
