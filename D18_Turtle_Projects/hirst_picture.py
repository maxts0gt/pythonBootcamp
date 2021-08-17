from turtle import Turtle, Screen, color, colormode
import random
turtle = Turtle()
screen = Screen()

colormode(255)
hist_color = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227),
              (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

turtle.penup()
turtle.color(random.choice(hist_color))


turtle.setx(-200)
y = -300
turtle.sety(y)
while y < 200:
    for i in range(10):
        turtle.sety(y)
        turtle.dot(20, random.choice(hist_color))
        turtle.forward(50)
    y += 50
    turtle.setx(-200)
turtle.hideturtle()
screen.exitonclick()
