import turtle

screen = turtle.Screen()


timmy = turtle.Turtle()


timmy.pensize(2)

def forward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def turn_left():
    timmy.left(5)


def turn_right():
    timmy.right(5)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


pen = True


def pen_up():
    global pen
    if pen:
        timmy.penup()
        pen = False
    else:
        timmy.pendown()
        pen = True


screen.listen()
screen.onkeypress(forward, 'Up')
screen.onkeypress(backward, 'Down')
screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')
screen.onkeypress(pen_up, 'space')
screen.onkeypress(clear, 'c')













screen.exitonclick()