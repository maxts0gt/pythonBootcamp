from turtle import Turtle
LINE_POSITION = 285


class Line:

    def __init__(self):
        LINE_POSITION = 285
        super().__init__()
        for line in range(0, int(280/20) + 1):
            self = Turtle('square')
            self.shapesize(0.80, 0.20)
            self.color('white')
            self.penup()
            self.setpos(0, LINE_POSITION)
            LINE_POSITION -= 40
