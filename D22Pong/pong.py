from turtle import Turtle
import random
WIDTH = 1000
HEIGHT = 600
SPEED = 5
INIT_ANGLE = random.choice([15,30,45,60,75])

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.left(INIT_ANGLE)
        self.speed(SPEED)


        # self.slope = random.randint(-2, 2)
        # self.const = 2

        # self.y = self.slope*self.x +self.const

        self.xlim, self.ylim = WIDTH/2-30, HEIGHT/2-30
        self.penup()

    # def move(self):
        # print(self.slope)
        # if not -self.xlimit < self.xcor() < self.xlimit:
        #     print("hello")
        #     self.slope = -self.slope
        # if not -self.ylimit < self.ycor() < self.ylimit:
        #     print("hellllllooy")
        #     self.slope = -self.slope
        #
        # self.x = self.xcor() + SPEED
        # self.y = self.x*self.slope
        #
        # self.goto(self.x, self.y)


        


