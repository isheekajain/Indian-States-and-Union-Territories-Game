import turtle
import pandas

screen = turtle.Screen()
screen.title("India States and Union Territories Game")

image = "India-map.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("states_uts.csv")
all_states = data.state_uts.to_list()
guess_states = []

while len(guess_states) < 28:
    ans = screen.textinput(title=f"{len(guess_states)}/36 States and Union Territories Correct",
                           prompt="What's another state's or union territory's name?").title()
    if ans == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guess_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_remind.csv")
        break
    if ans in all_states:
        guess_states.append(ans)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state_uts == ans]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans)








