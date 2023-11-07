from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x, y)
        self.score = 0

    def game_over(self):
        self.color("red")
        self.write(f"Game Over", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 24, "normal"))
