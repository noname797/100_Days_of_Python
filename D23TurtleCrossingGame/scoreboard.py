FONT = ("Courier", 24, 'normal')
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-280, 260)
        self.write_on()
        self.hideturtle()

    def write_on(self):
        self.write(f"Level: {self.level}", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.write_on()

    def end(self):
        bruh = Turtle()
        bruh.penup()
        bruh.goto(-80,0)
        bruh.write("Game Over", font= FONT)
        bruh.hideturtle()


