from telnetlib import DO
from turtle import Turtle, up
UP = 90
DOWN = 270
DISTANCE = 40
STR_WIDTH, STR_LENGTH, STR_OUTLINE = 1, 5, 1 
UP_EDGE = 240
DOWN_EDGE = -240


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
        self.color('white')
        self.penup()
        self.setheading(UP)
    
    def create_player(self):
        self.shape('square')
        self.shapesize(STR_WIDTH, STR_LENGTH, STR_OUTLINE)
        
    def go_up(self):
        if self.ycor() < UP_EDGE:
            self.setheading(UP)
            self.forward(DISTANCE)
    
    def go_down(self):
        # print(self.ycor())
        if self.ycor() > DOWN_EDGE :
            self.setheading(DOWN)
            self.forward(DISTANCE)

    

