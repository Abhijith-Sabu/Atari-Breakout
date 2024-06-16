from paddle_module import Paddle
from Ball_module import Ball
from object_module import Object
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
    blocks = []
    block_positions = [(x, y) for y in range(250, 200, -20) for x in range(-350, 400, 80)]
    print(block_positions)
    for position in block_positions:
        block = Object(position)
        blocks.append(block)



    
    
    paddle.goto(0, -250) # Position the paddle at the right edge of the screen
    screen.cv.bind('<Motion>',lambda event: paddle.on_mouse_move(event.x,event.y))




    while True:
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
                ball.bounce_y()
                block.hideturtle()  # Hide the block upon collision
                blocks.remove(block)  # Remove the block from the list
        if len(blocks)==0:
            print('you won ')







if __name__ == "__main__":
    main()
