from tkinter import font
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scorboard(Turtle):
    def __init__(self):
        super().__init__() # Can do anything that Turtle can do
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write_on()

    def write_on(self):
        self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

        

    def update_score(self):
        self.clear() # Else it overwites
        self.score += 1
        self.write_on()  


    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over.', align=ALIGNMENT, font= FONT)

    