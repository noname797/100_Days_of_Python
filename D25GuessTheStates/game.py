import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)
turtle.penup()

game_on = True

count = 0
states = []
while game_on:
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    answer_state = screen.textinput(title=f'Guess the {len(states)}/50 State', prompt="What's another state's name?")
    if answer_state.capitalize() in data['state'].values:
        x = data[data.state == answer_state.capitalize()]['x'].values[0]
        y = data[data.state == answer_state.capitalize()]['y'].values[0]
        new_turtle.goto(x,y)
        new_turtle.write(answer_state.capitalize())
        count += 1

        if answer_state.capitalize() not in states:
            states.append(answer_state.capitalize())

    if answer_state.capitalize() == 'Exit':
        missing_states = [state for state in data['state'].values if state not in states]
        # for state in data['state'].values:
        #     if state not in states:
        #         missing_states.append(state)
        game_on = False
        pd.DataFrame(missing_states).to_csv("States_to_learn.csv")


    if count == 50:
        game_on = False
        end = turtle.Turtle()
        end.hideturtle()
        end.write("Game Over. You won.")




screen.exitonclick()

# Ideas :
# * one for your own country or the whole world
# * we can do find in images game, naming all animals/plants
