# Imports 
from turtle import Turtle
import random


class Food(Turtle):  # here food class is inheriting all the properties of turtle class therefore Food(Turtle) is used

    def __init__(self):
        super().__init__()  # using this, we inherit all the turtle class functions

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # since default size of circle is (20,20) so we are reducing it to (10,10)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

