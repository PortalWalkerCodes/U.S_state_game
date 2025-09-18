import turtle
import pandas
from tkinter import messagebox
import os
import sys

screen = turtle.Screen()
screen.setup(725, 491)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
states = data.state

image = "blank_states_img.gif"

screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
screen.update()

state_drawer = turtle.Turtle()
state_drawer.hideturtle()
state_drawer.penup()


game_is_on = True
score = 0
already_guessed =  []
not_guessed = {"not_guessed_states": []}



while game_is_on:
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name? Type 'Exit' when you are done.").title()

    for state in states:
        if state == answer_state:
            state_data = data[data.state == state]

            x = int(state_data.x)
            y = int(state_data.y)

            if answer_state not in already_guessed:
                state_drawer.goto(x, y)
                state_drawer.write(f"{answer_state}")
                score += 1
                already_guessed.append(answer_state)
                screen.update()
                break
            else:
                messagebox.showwarning("Already guessed.", f"You already guessed {answer_state}.\nPlease try again with a different state.")


            if score == 50:
                messagebox.showinfo("You win!", "You win!")
                game_is_on = False
                break
            break

        elif answer_state == "Exit":
            game_is_on = False
            for each in states:
                if each not in already_guessed:
                    not_guessed["not_guessed_states"].append(each)
            df = pandas.DataFrame(not_guessed)
            df.to_csv(path_or_buf="states_to_learn.cvs", mode="w")

            file_path = os.path.abspath("states_to_learn.cvs")
            messagebox.showinfo("Results!", f"Your total score is: {score}/50.\nThe states you missed are in {file_path}.\nPlease try again for a perfect score.")
            turtle.bye()
            sys.exit(0)



    else:
        messagebox.showwarning("State does not exist.", f"The state of {answer_state} does not exist.\nPlease try again with a different state.")

turtle.mainloop()