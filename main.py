from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

screen.listen()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.paddle_collision()

    if ball.xcor() > 380:
        ball.out_of_bounds()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.out_of_bounds()
        scoreboard.r_point()

screen.exitonclick()