from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1.0, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.setpos(260, (random.choice(range(-250, 250))))
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT