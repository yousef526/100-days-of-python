from turtle import Screen 
import random
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title(titlestring="My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.goUp,'Up')
screen.onkey(snake.goDown,'Down')
screen.onkey(snake.leftward,'Left')
screen.onkey(snake.rightward,'Right')
game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.detect_wall():
        scoreboard.reset_score()
        snake.reset_snake()
        #game_is_on = False
        #scoreboard.gameOver()
    
    # detection on collsion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.on_score()
        snake.extend_tail()

    for i in range(1,len(snake.squares)-1,1):
        if snake.head.distance(snake.squares[i]) < 10:
            scoreboard.reset_score()
            snake.reset_snake()
            #game_is_on = False
            #scoreboard.gameOver()
    
    
    

screen.exitonclick()