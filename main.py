import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(player.move_player_up, "Up")

game_is_on = True
counter = 0


while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1

    # create a car every 6th loop
    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # player collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            level.game_over()

    # player reaches top
    if player.ycor() > 280:
        level.add_level()
        car_manager.increase_speed()
        player.reset_player()

screen.exitonclick()
