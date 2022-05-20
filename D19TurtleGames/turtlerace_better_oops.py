import random
from turtle import Turtle, Screen


class TurtleRace:
    def __init__(self):
        self.colors = ['green', 'yellow', 'blue', 'pink', 'orange', 'red']
        self.race_on = False
        self.all_turtles = []
        self.winner = ''
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.user_bet = ''

    def user_in(self):
        self.user_bet = self.screen.textinput(title="Place your bet.", prompt="Enter the color of the turtle: ")
        if self.user_bet:
            self.race_on = True

    def initialisation(self):
        y_pos = -150
        for i in range(len(self.colors)):
            timmy = Turtle(shape='turtle')
            timmy.color(self.colors[i])
            timmy.penup()
            timmy.goto(x=-230, y=y_pos)
            y_pos += 60
            self.all_turtles.append(timmy)

    def game_on(self):
        while self.race_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 230:
                    self.winner = turtle.pencolor()
                    self.race_on = False
                    if self.winner == self.user_bet:
                        print(f"You've won! The {self.winner} turtle is the winner!")
                    else:
                        print(f"You've lost! The {self.winner} turtle is the winner!")

                distance = random.randint(0,10)
                turtle.forward(distance)

        self.screen.exitonclick()


if __name__ == "__main__":
    game = TurtleRace()
    game.user_in()
    game.initialisation()
    game.game_on()
