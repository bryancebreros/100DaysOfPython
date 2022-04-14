import turtle
import pandas

screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Guess {len(guessed_states)}/50", prompt="State name?").title()
    if answer == "Exit":
        missing = []
        for i in states:
            if i not in guessed_states:
                missing.append(i)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("states_missing.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


screen.exitonclick()