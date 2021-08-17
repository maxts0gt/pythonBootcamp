import turtle as t
import random
turtle = t.Turtle()
screen = t.Screen()
turtle.shape('turtle')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


random_walk = [0, 90, 180, 270]
turtle.pensize(15)
turtle.speed('fastest')

for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(random_walk))
