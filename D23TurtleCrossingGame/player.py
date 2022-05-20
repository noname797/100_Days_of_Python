from turtle import Turtle


START = (0, -280)
DISTANCE = 10
END = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(START)
        self.shape('turtle')

    def move_up(self):
        if self.ycor() != END:
            self.forward(DISTANCE)

    def move_down(self):
        if self.ycor() != START[1]:
            self.back(DISTANCE)
