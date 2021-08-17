from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
turtle.shape('turtle')
turtle.color('black')

colours = ['red', 'blue', 'green', 'yellow',
           'brown', 'IndianRed', 'grey', 'orange']


def draw_shape(number):
    angle = 360 / number
    for _ in range(number):
        turtle.forward(100)
        turtle.right(angle)


for times in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shape(times)
