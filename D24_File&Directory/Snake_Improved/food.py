from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        next_location_x = random.randint(-280, 280)
        next_location_y = random.randint(-280, 280)
        self.goto(next_location_x, next_location_y)
        self.refresh()

    def refresh(self):
        next_location_x = random.randint(-280, 280)
        next_location_y = random.randint(-280, 280)
        self.goto(next_location_x, next_location_y)
