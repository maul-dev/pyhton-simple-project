from data import *
from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        snake = []
        for position in START_POSITION:
            snake.append(self.add_segment(position))
        return snake

    @staticmethod
    def add_segment(position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        return new_segment

    def move(self):
        for seg_index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_index-1].xcor()
            new_y = self.segments[seg_index-1].ycor()
            self.segments[seg_index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
