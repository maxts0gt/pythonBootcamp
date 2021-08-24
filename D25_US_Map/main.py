from turtle import Turtle, Screen
import pandas as pd
FONT = ("Courier", 10, "normal")
locator = Turtle()
locator.hideturtle()
locator.penup()
outside_handler = Turtle()
screen = Screen()
screen.title('U.S. States Game')
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
outside_handler.shape(image)
data = pd.read_csv("us-states-game-start/50_states.csv")
data = pd.DataFrame(data)
list = data["state"]
list_states_lower = [word.lower() for word in list]
print(list_states_lower)


def get_mouse_click_coor(x, y):
    print(x, y)


count = 0
answer_list = []
unanswered_list = []
while count != 50:
    answer = screen.textinput(
        title=f"{count}/50 States Correct", prompt="What's another state's name")
    answer_lower = answer.lower()
    if answer_lower not in answer_list and answer_lower in list_states_lower:
        answer_list.append(answer_lower)
        count = len(answer_list)
        choice = data[data.state.str.lower() == answer_lower]
        locator.goto(int(choice.x), int(choice.y))
        locator.write(f"{answer_lower.title()}", align="left", font=FONT)
    elif answer_lower == "exit":
        for state in list_states_lower:
            if state in answer_list:
                pass
            else:
                unanswered_list.append(state)
                data = pd.DataFrame("states", unanswered_list)
                data.to_csv("list_of_states_to_learn.csv")

        break


outside_handler.mainloop()
