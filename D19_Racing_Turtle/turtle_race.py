from turtle import Turtle, Screen, color
from random import randint
all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "black", "purple"]
screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet",
                       prompt="We have 7 racing turtles. Choose the color of the turtle who you think will win? ")


if bet:
    is_race_on = True


def move_forward_randomly(turtle):
    turtle = Turtle().forward(randint(0, 10))


i = 0
y_position = 120

for turtle in range(len(colors)):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y_position)
    i += 1
    y_position -= 40
    all_turtles.append(turtle)


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == bet:
                print(f'Congrats you won! The turtle {winner_color} has won!')
            else:
                print(f'You lose! The turtle {winner_color} has won!')
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
