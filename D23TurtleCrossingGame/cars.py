from turtle import Turtle
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
CORDINATES = []
MOVE_DISTANCE = 5
INCREMENTS = 10

y = -250
while y < 260:
    CORDINATES.append(y)
    y += 50


class Cars:
    def __init__(self):
        self.all_cars = []
        self.speed = 20

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.choice(CORDINATES)
            new_car.goto(300, y_cor)
            new_car.speed(self.speed)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

    def levelup(self):
        self.speed += 20

