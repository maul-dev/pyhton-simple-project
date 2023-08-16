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
scoreboard = Scoreboard((-290, 260))

screen.listen()
screen.onkeypress(fun=player.up, key="w")
screen.onkeypress(fun=player.up, key="Up")
time_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_speed)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.cars_list:
        if car.xcor() < -290:
            car.clear()
            car.hideturtle()
            cars.cars_list.remove(car)
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_finish():
        player.start_position()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
