import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('black')

# Draw square
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

# Draw dashed lines.

for i in range(10):
    timmy.color("black")
    timmy.forward(10)
    timmy.color("white")
    timmy.forward(10)

timmy.color("black")

for i in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# Drawing shapes

colours = ['black', 'pink', 'purple', 'gold', 'tomato', 'skyblue',"CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_polygons(num=10):
    sides = 3
    for i in range(num-sides+1):
        timmy.color(random.choice(colours))
        for j in range(sides):
            timmy.forward(100)
            timmy.right(360/sides)
        sides += 1


draw_polygons()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

timmy.pensize(15)
timmy.shape('circle')
timmy.speed('fastest')

angles = [0, 90, 180, 270]


def random_color():
    out = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return out


turtle.colormode(255)
for i in range(200):
    timmy.right(random.choice(angles))
    timmy.color(random_color())
    timmy.forward(30)


def random_color():
    out = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return out


timmy.shape('classic')
timmy.speed('fastest')
turtle.colormode(255)

for i in range(100):
    timmy.circle(100)
    timmy.color(random_color())
    timmy.left(6)

# OR
turtle.colormode(255)
timmy.speed('fastest')


def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


draw_spirograph(8)

screen = Screen()
screen.exitonclick()
