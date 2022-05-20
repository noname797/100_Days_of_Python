from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 50, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pensize(5)
        self.penup()
        self.goto(0, 280)
        self.setheading(270)
        self.pendown()
        self.hideturtle()

        while self.ycor() > -280:
            # print(self.ycor())
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(15)

        self.score = 0


    def write_on(self):
        self.write(f"{self.score}", align = ALIGNMENT, font = FONT)


    def print_score(self):
        self.penup()
        self.write_on()

    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write_on()

    
        