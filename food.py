from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.pos_x = None
        # self.pos_y = None
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.cors_seg_of_snake = [(0, 0), (-20, 0), (-40, 0)]
        self.refresh()

    def add_seg_of_snake(self, cors):
        """cors mast have '(turtle.xcor(), turtle.ycor()'"""
        self.cors_seg_of_snake.append(cors)

    def refresh(self):
        pos_x = random.randint(-480, 470)
        pos_y = random.randint(-480, 470)
        if self.check_refresh(pos_x, pos_y):
            self.refresh()
        else:
            self.goto(pos_x, pos_y)


    def check_refresh(self, x, y):
        xy = (x, y)
        if xy in self.cors_seg_of_snake:
            return True
        else:
            return False
