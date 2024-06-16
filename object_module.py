import random
from turtle import Turtle


colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta", 
          "lime", "maroon", "navy", "olive", "teal", "violet", "turquoise", "gold", "silver", "grey"]

class Object(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.color(random.choice(colors))