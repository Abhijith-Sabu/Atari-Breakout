from paddle_module import Paddle
from Ball_module import Ball
from object_module import Object
from score_module import Score
import turtle
import time

def main():
    screen = turtle.Screen()
    screen.bgcolor("#333333")
    screen.setup(width=800, height=600)
    screen.title("Atari Breakout")
    screen.tracer(0)
    
    

    paddle = Paddle()
    ball=Ball()
    score=Score()

    blocks = []
    block_width = 80  # Width of each block
    block_height = 20  # Height of each block
    gap = 10  # Gap between blocks
    
    start_x = -350  # Starting X position
    start_y = 250  # Starting Y position
    
    block_positions=[(x,y)for y in range(start_y, 200, -block_height - gap) for x in range(start_x, 400, block_width + gap)]
    for position in block_positions:
        block = Object(position)
        blocks.append(block)
    
    
    paddle.goto(0, -250) # Position the paddle at the right edge of the screen
    screen.cv.bind('<Motion>',lambda event: paddle.on_mouse_move(event.x,event.y))



    game =True
    while game:
        time.sleep(ball.speed_of_ball)
        screen.update()
        ball.move()

        if ball.ycor() >290 or ball.ycor() <-300:
            ball.reducespeed()
   
 

        if ball.xcor() >390 or ball.xcor() <-400:
            ball.bounce_x()
            
        if (ball.distance(paddle) < 50 and ball.ycor() < -240 and ball.ycor() > -250):
            ball.bounce_y()
        for block in blocks:
            if ball.distance(block) < 30:
                score.point()
                ball.bounce_y()
                block.hideturtle()  # Hide the block upon collision
                blocks.remove(block)  # Remove the block from the list
        if len(blocks)==0:
            print('you won ')
            game=False







if __name__ == "__main__":
    main()
