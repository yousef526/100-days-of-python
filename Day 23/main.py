import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
score = Scoreboard()
cars_manger = CarManager()

screen.listen()
screen.onkeypress(user.moveUp,'Up')
screen.onkeypress(user.moveDown,'Down')

game_is_on = True
create_car = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manger.move()
    if create_car % 6 == 0:
        cars_manger.createcar()

    # check if win race to increase the speed of cars
    if user.ycor() >= 280:
        user.go_start_state()
        cars_manger.inc_speed()
        score.inc_level()

    # detect collsion with cars
    for car in cars_manger.cars:
        if user.distance(car) >= 5 and user.distance(car) < 20:
            game_is_on = False
            score.game_Over()


    create_car+=1
    
   
screen.exitonclick()