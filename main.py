import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting the list of states from the csv file
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

# Use a loop to allow the user to keep guessing
correct_answers = []
while len(correct_answers) < 50:
    # Getting user input
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()
    # Check if user input is among the 50 states
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in correct_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states) # One column DataFrame
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list and answer_state not in correct_answers:
        correct_answers.append(answer_state)

        state_data = data[data.state == answer_state] # The entire row of the specific state
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x=state_data.x.item(), y=state_data.y.item())
        t.write(answer_state)
