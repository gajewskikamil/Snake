from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.pos_x = None
        self.pos_y = None
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.pos_x = random.randint(-480, 480)
        self.pos_y = random.randint(-480, 480)
        self.goto(self.pos_x, self.pos_x)
