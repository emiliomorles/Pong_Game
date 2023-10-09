from turtle import Screen
from players import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong by @Emilio_Morles")
screen.tracer(0)  # https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer

paddle_r = Paddle((350, 0), "white")
paddle_l = Paddle((-350, 0), "lime")
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # This is the speed that the screen updates.
    screen.update()  # It updates the screen.tracer(0) in order to avoid the animation that
    # move the paddle to the right from the middle of the screen
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:  # It detects collision with roof or floor
        ball.bounce_y()

    if ball.distance(paddle_r) < 85 and ball.xcor() > 310 or ball.distance(paddle_l) < 85 and ball.xcor() < -310:
        # It detects collision with the paddle
        ball.bounce_x()

    if ball.xcor() > 380:  # It detects when right paddle misses the ball.
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:  # It detects when left paddle misses the ball.
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
