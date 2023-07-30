# 두려움을 내버려두고 하고 싶은 일에 에너지를 집중하자

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard1 import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0) # 화면 객체. 애니메이션 효과 끄기. 0.

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up") # go_up() 하면 안됨
screen.onkey(r_paddle.go_down, "Down") # go_up() 하면 안됨
screen.onkey(l_paddle.go_up, "w") # go_up() 하면 안됨
screen.onkey(l_paddle.go_down, "s") # go_up() 하면 안됨

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #nees to bounce
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # print("Made contact")

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()