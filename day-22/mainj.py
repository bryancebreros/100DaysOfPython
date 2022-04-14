from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
paddler = Paddle(350, 0)
paddlel = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddler.up, "Up")
screen.onkey(paddler.down, "Down")
screen.onkey(paddlel.up, "w")
screen.onkey(paddlel.down, "s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(paddler) < 50 and ball.xcor() > 320) or (ball.distance(paddlel) < 50 and ball.xcor() < -320):
        ball.collision()
    if ball.xcor() > 380:
        score.l_point()
        ball.reset()

    elif ball.xcor() < -380:
        score.r_point()
        ball.reset()


screen.exitonclick()
