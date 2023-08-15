import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard((-230, 260))

screen.listen()
screen.onkeypress(fun=player.up, key="w")
screen.onkeypress(fun=player.up, key="Up")

time_speed = 0.1
counter = 0
game_is_on = True
while game_is_on:
    time.sleep(time_speed)
    screen.update()
    cars.move()
    counter += 1
    if counter % 6 == 0:
        cars.add_cars()

    for car in cars.cars_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_finish():
        player.reset_position()
        cars.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
