from paddle_module import Paddle
from Ball_module import Ball
from object_module import Object
from score_module import Score
import turtle
import time
from turtle import Turtle
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
    global youWon
    youWon=False

    game_is_on = True
    you_won = False


    while game_is_on:
        time.sleep(ball.speed_of_ball)
        screen.update()
        ball.move()

        if ball.ycor() <-300:
            ball.reducespeed()
        if ball.ycor()>290:
            ball.bounce_y()
   
 

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
            you_won = True
            game_is_on = False
    

    # End game screen
    screen.clear()
    screen.bgcolor("#333333")
    end_message = Turtle()
    end_message.color("white")
    end_message.penup()
    end_message.hideturtle()
    if you_won:
        end_message.write("You Won", align='center', font=("consolas", 80, "normal"))
    else:
        end_message.write("Game Over", align='center', font=("consolas", 80, "normal"))
    turtle.done()


if __name__ == "__main__":
    main()
