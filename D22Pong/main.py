from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from pong import Pong
import time


screen = Screen()

screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.title('PingPong')
screen.tracer(0)

p1 = Player()
p2 = Player()
pong = Pong()

p1_score = ScoreBoard()
p2_score = ScoreBoard()

p1_score.goto(-50, 220)
p1_score.print_score()
p2_score.goto(50, 220)
p2_score.print_score()


p1.goto(-485,0)
p2.goto(480,0)

screen.listen()
screen.onkey(p1.go_up, 'w')
screen.onkey(p1.go_down, 's')
screen.onkey(p2.go_down, 'Down')
screen.onkey(p2.go_up, 'Up')

game_on = True


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 40 and abs(a.ycor() - b.ycor()) < 40


while game_on:
    screen.update()


    x = pong.xcor()
    y = pong.ycor()

    print(x, y)

    print(pong.distance(p1))

    if is_collided_with(pong, p1) or is_collided_with(pong, p2):
        if is_collided_with(p1, pong):
            p1_score.update_score()
        elif is_collided_with(pong, p2):
            p2_score.update_score()

        head = pong.heading()
        pong.setheading(180 - head)

    if abs(x) >= pong.xlim:
        break
        # head = pong.heading()
        # pong.setheading(180 - head)

    if abs(y) >= pong.ylim:
        head = pong.heading()
        pong.setheading(-head)

    pong.forward(10)

    time.sleep(0.03)











#
#
#
#
# while game_on:
#     screen.update()
#     time.sleep(0.03)
#
#     if y < -pong.ylimit:
#         pong.
#
#     pong.goto(x, y)
#     x = pong.xcor() + 2
#     y = pong.slope * x
#
#
#
#
#
#     else:
#
#         pong.c = pong.ycor() + pong.slope * pong.xcor()
#         print(pong.c)
#         y = -pong.slope*x + pong.c
#         print(y)
#         pong.goto(x, y)
#         x = pong.xcor() + 2
#
#
#
#
#
#     # if not -pong.xlimit < pong.x < pong.xlimit:
#     #     print("hello")
#     #     break
#     #
#     # elif no -pong.ylimit > pong.y < pong.ylimit:
#     #     print("heloooyyy")
#     #     pong.slope = -pong.slope
#     #     pong.x = pong.xcor() + 2
#     #     pong.c = pong.ycor() -pong.slope*pong.xcor()
#     #     pong.y = pong.x*pong.slope + pong.c
#     #     pong.goto(pong.x, pong.y)
#     # else:
#     #     pong.move()
#     #     print(pong.xcor())
#     #     print(pong.ycor())
#
#
#
#

screen.exitonclick()