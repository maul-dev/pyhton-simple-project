from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.start_position()

    def up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def is_finish(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def start_position(self) -> None:
        self.setheading(90)
        self.goto(STARTING_POSITION)
