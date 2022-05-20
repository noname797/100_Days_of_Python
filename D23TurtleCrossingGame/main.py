import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
car = Cars()
score = Scoreboard()


screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')


game_on = True



while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    if player.ycor() == 280:
        score.update_score()
        player.goto((0, -280))
        car.levelup()

    dum = car.all_cars

    for i in dum:
        if i.xcor() < -350:
            car.all_cars.pop(car.all_cars.index(i))

    for i in car.all_cars:
        if player.distance(i) < 25:
            game_on = False
            score.end()


screen.exitonclick()
