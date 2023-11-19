import pandas as pd
import turtle 

df = pd.read_csv('50_states.csv')
#print(df[df['state'] == 'Alabama'])

states = df['state'].to_list()
screen = turtle.Screen()
screen.bgpic('blank_states_img.gif')
screen.title("Welcome to USA map")


def write_state(state_name,x,y):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x,y)
    tim.write(state_name)


correct_guesses = []
while len(correct_guesses) < len(states):
    user_input = screen.textinput(title=f'{len(correct_guesses)}/{len(states)}',
                                  prompt='Enter a name of state:').title()
    if user_input in states:
        coordinates = df[df['state'] == user_input]
        x_coordinate = int(coordinates.x)
        y_coordinate = int(coordinates.y)
        write_state(user_input.title(),x_coordinate,y_coordinate)
        correct_guesses.append(user_input)

    elif user_input =='Exit':
        states_to_learn = [item for item in states if item not in correct_guesses]
        states_to_learn = pd.DataFrame(states_to_learn)
        states_to_learn.to_csv('new_learned.csv')
        break

screen.exitonclick()