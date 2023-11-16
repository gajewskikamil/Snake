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
        with open("score.txt", "r") as file:
            self.high_score = int(file.read())

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.color("red")
    #     self.write(f"Game Over", move=False, align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 24, "normal"))
