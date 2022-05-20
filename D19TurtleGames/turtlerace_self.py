import turtle
import random
import numpy


class TurtleRace:
    def __init__(self):
        self.green = turtle.Turtle()
        self.green.color('green')
        self.green.shape('turtle')
        self.green.penup()
        self.green.speed('normal')
        self.green_distance = 0

        self.red = turtle.Turtle()
        self.red.color('red')
        self.red.shape('turtle')
        self.red.penup()
        self.red.speed('normal')
        self.red_distance = 0

        self.blue = turtle.Turtle()
        self.blue.color('blue')
        self.blue.shape('turtle')
        self.blue.penup()
        self.blue.speed('normal')
        self.blue_distance = 0

        self.yellow = turtle.Turtle()
        self.yellow.color('yellow')
        self.yellow.shape('turtle')
        self.yellow.penup()
        self.yellow.speed('normal')
        self.yellow_distance = 0

        self.black = turtle.Turtle()
        self.black.color('black')
        self.black.shape('turtle')
        self.black.penup()
        self.black.speed('normal')
        self.black_distance = 0

        self.pink = turtle.Turtle()
        self.pink.color('pink')
        self.pink.shape('turtle')
        self.pink.penup()
        self.pink.speed('normal')
        self.pink_distance = 0
        
        self.turtles = [self.green, self.red, self.blue, self.yellow, self.black, self.pink]
        self.speeds = ['slowest']  # ['slow', 'slowest']
        self.distance = numpy.arange(50, 101, 10)
    
    def start_position(self):
        turtle_copy = self.turtles
        i = random.choice(turtle_copy)
        turtle_copy.pop(turtle_copy.index  (i))
        i.setheading(135)
        i.forward(500)
        i.setheading(0)

        diff = 135
        for _ in range(len(turtle_copy)):
            i = random.choice(turtle_copy)
            turtle_copy.pop(turtle_copy.index(i))
            i.setheading(135)
            i.forward(500)
            i.setheading(270)
            i.forward(diff)
            i.setheading(0)
            diff += 135

    def win(self, x):
        return x >= 700

    def popup(self):
        return screen.textinput('Make your bet', "who will win the race? Enter a color: ")

    def begin_race(self):
        gameon = True
        while gameon:
            self.turtles = [self.green, self.red, self.blue, self.yellow, self.black, self.pink]
            turtle_copy = self.turtles
            for _ in range(len(turtle_copy)):
                i = random.choice(turtle_copy)
                turtle_copy.pop(turtle_copy.index(i))
                if i == self.green:
                    x = random.choice(self.distance)
                    self.green_distance += x

                    if self.win(self.green_distance):
                        gameon = False
                        self.green.forward(self.green_distance - 700)
                        self.green.speed('fastest')
                        print("Green Won")
                        print(self.green_distance)
                        break

                    self.green.speed(random.choice(self.speeds))
                    self.green.forward(x)

                elif i == self.red:

                    x = random.choice(self.distance)

                    self.red_distance += x

                    if self.win(self.red_distance):
                        gameon = False
                        self.red.forward(self.red_distance - 700)
                        self.red.speed('fastest')
                        print("Red Won")
                        print(self.red_distance)
                        break

                    self.red.speed(random.choice(self.speeds))
                    self.red.forward(x)

                elif i == self.blue:

                    x = random.choice(self.distance)

                    self.blue_distance += x

                    if self.win(self.blue_distance):
                        gameon = False
                        self.blue.forward(self.blue_distance - 700)
                        self.blue.speed('fastest')
                        print("Blue Won")
                        print(self.blue_distance)
                        break

                    self.blue.speed(random.choice(self.speeds))
                    self.blue.forward(x)

                elif i == self.yellow:

                    x = random.choice(self.distance)

                    self.yellow_distance += x

                    if self.win(self.yellow_distance):
                        gameon = False
                        self.yellow.forward(self.yellow_distance - 700)
                        self.yellow.speed('fastest')
                        print("Yellow Won")
                        print(self.yellow_distance)
                        
                        break
                        

                    self.yellow.speed(random.choice(self.speeds))
                    self.yellow.forward(random.choice(self.distance))

                elif i == self.black:

                    x = random.choice(self.distance)

                    self.black_distance += x

                    if self.win(self.black_distance):
                        gameon = False
                        self.black.forward(self.black_distance - 700)
                        self.black.speed('fastest')
                        print("Black Won")
                        print(self.black_distance)

                        break

                    self.black.speed(random.choice(self.speeds))
                    self.black.forward(x)

                elif i == self.pink:

                    x = random.choice(self.distance)

                    self.pink_distance += x

                    if self.win(self.pink_distance):
                        gameon = False
                        self.pink.forward(self.pink_distance - 700)
                        self.pink.speed('fastest')
                        print("Pink Won")
                        print(self.pink_distance)
                        break

                    self.pink.speed(random.choice(self.speeds))
                    self.pink.forward(x)


if __name__ == "__main__":
    screen = turtle.Screen()
    game = TurtleRace()
    inn = game.popup()
    game.start_position()
    game.begin_race()
    screen.exitonclick()
