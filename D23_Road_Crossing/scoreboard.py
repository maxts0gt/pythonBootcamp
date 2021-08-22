from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    pass

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-60, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align='left',
                   font=FONT)

    def score_counter(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", font=FONT)
