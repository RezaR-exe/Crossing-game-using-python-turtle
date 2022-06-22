from turtle import Turtle


font = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

    def WriteScore(self):
        self.goto(-150, 270)
        self.write(f"Level: {self.score}", font=font)

    def GameOver(self):
        self.goto(0, 0)
        self.write("Game over!", font=font)

    def IncrementScore(self):
        self.score += 1
        self.clear()
        self.WriteScore()
