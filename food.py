import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Erase the current food (if any) and spawn a new one at a random position"""
        self.color(random.randint(10, 245), random.randint(10, 245), random.randint(10, 245))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
