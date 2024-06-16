from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score1=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(x=0,y=256)
        self.write(self.score1,align='center',font=("consolas",30,"normal"))
        
    def point(self):
        self.score1+=7
        self.update_score()