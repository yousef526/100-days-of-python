from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

tim = Turtle()
tim.color('red')
tim.hideturtle()

def draw_dashed_line():
    tim.penup()
    tim.goto(0,330)
    tim.right(90)
    while tim.ycor() >= -350:
        tim.pendown()
        tim.forward(30)
        tim.penup()
        tim.forward(30)
        

screen = Screen()
screen.bgcolor('black')
screen.setup(width=700,height=700)
screen.tracer(0)

# draw dashed line in screen
draw_dashed_line()

player_1 = Paddle(-330,0)# on left
player_2 = Paddle(330,0)# on right
score_player1 = Score(-50,310)
score_player2 = Score(50,310)
ball = Ball()


screen.listen()
screen.onkey(player_1.moveUp,'w')
screen.onkey(player_1.moveDown,'s')
screen.onkey(player_2.moveUp,'Up')
screen.onkey(player_2.moveDown,'Down')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.moving()# to move ball
    #if snake.head.distance(food) < 15

    # detect collsion with wall
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()
        
    # detect collsion with the paddle
    if ball.distance(player_1) < 50 and ball.xcor() < -300 or ball.distance(player_2) < 50 and ball.xcor() > 300:
        ball.bounce_x()
        if ball.x_move > 0:
            ball.x_move+=5
        else:
            ball.x_move-=5

    # detect if ball gone off limit
    if ball.xcor() >= 350:
        score_player1.inc_score()
        ball.reset_ball()
    elif ball.xcor() <= -350:
        score_player2.inc_score()
        ball.reset_ball()
    
    if score_player1.score >= 10 or score_player2.score >= 10:
        ball.write("Game over",move=False,align='center', font=('Aerial', 24, 'normal'))
        game_on = False

screen.exitonclick()