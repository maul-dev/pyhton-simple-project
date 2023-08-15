import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()

screen.listen()
screen.onkeypress(fun=player.up, key="w")
screen.onkeypress(fun=player.up, key="Up")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter % 6 == 0:
        car.add_cars()
    car.move()
    if player.is_finish():
        player.reset_position()
