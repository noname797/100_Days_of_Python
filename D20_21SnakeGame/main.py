import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scorboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen until screen is updated


snake = Snake()
food = Food()
scoreboard = Scorboard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on =False
            scoreboard.game_over()



    
    




screen.exitonclick()

# for segment in segments:
#     segment.forward(20)
#     # time.sleep(1) # Introduces sleep/ delay of 1sec after each update
