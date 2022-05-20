from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y_pos = -150

for turtles in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtles])
    tim.penup()
    tim.goto(x=-230, y=y_pos)
    y_pos += 60

    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_on = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        distance = random.randint(0,10)
        turtle.forward(distance) 

screen.exitonclick()