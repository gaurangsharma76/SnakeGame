from turtle import Turtle
import random


class food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.food_location()

    def food_location(self):
        food_x = random.randint(-270, 270)
        food_y = random.randint(-270, 270)
        self.goto(food_x, food_y)
