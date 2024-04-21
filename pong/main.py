#TODO 1 -- set the screen; length, width, pixels etc.
#TODO 2 -- draw the vertical line to divide the screen
#TODO 3 -- create 2 turtles who will be paddles; controlled up/down motion
#TODO 4 -- the ball spawns in the middle; it randomly goes towards one side
#TODO 5 - IDK HOW ITS BOUNCING!
#TODO 6 - when the ball goes through screen edge, the opposite user scores
#TODO 7 -- scoreboard which displays points
#TODO 8 -- the ball respawns every time someone scores

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()

r_paddle = Paddle((350, 0))
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

l_paddle = Paddle((-350, 0))
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


ball = Ball()
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with ceiling/floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Ball goes out of bounds // r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Ball goes out of bounds // l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()