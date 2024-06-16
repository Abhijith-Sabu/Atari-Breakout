from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('pale turquoise')
        
        self.penup()
        self.goto(0, -230)
        self.xmove=5
        self.ymove=5
        self.speed_of_ball=0.1


    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ymove*=-1
        self.speed_of_ball*=0.9
    def bounce_x(self):
        self.xmove*=-1
        self.speed_of_ball*=0.9
    def reducespeed(self):
        self.ymove*=-1
        self.speed_of_ball*=9

  

    def speed_of_ball(self):
        self.speed(5)