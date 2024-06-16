# paddle_module.py

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.left(90)
        self.shapesize(stretch_wid=5, stretch_len=1)
       

        self.color("pale turquoise")
        self.penup()


    def on_mouse_move(self,x,y):
        self.goto(x-400,self.ycor())

