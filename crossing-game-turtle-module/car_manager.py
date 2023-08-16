from random import randint, choice
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def level_up(self):
        self.speed += MOVE_INCREMENT

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(randint(280, 300), randint(-230, 230))
            self.cars_list.append(new_car)

    def move(self):
        for car in self.cars_list:
            car.forward(self.speed)
