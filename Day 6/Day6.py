# to write a function

def my_fun():
    print("Hello my love")

my_fun()

# in robot game  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
##############################
#exericse 1 
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#turn_left()
#move()
#turn_right()
#move()
#turn_right()
#move()
#turn_right()
#move()
"""
###################################

#exercise 2
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()
    
def way_to_goal():
    move()
    if wall_in_front():
       turn_left()
       move()
       go_right()
       start_place()
       turn_left()
def start_place():
    move()
    go_right()
    move()
    go_right
    pass
while True:
    way_to_goal()
    if at_goal():
        break
"""

#####################################
#exercise 3
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()
def obstacle_check():
    if wall_in_front():
        turn_left()
        move()
        go_right()
        move()
        go_right()
        move()
        turn_left()
while True:
    obstacle_check()
    if not wall_in_front() and not at_goal():
        move()
    if at_goal():
        break
"""

###############################################
#exercise 4
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()
def obstacle_check():
    if wall_in_front():
        turn_left()
        dist = climb_height()##
        go_right()
        move()
        go_right()
        get_down(dist)##
        turn_left()
def climb_height():
    distance = 0
    while wall_on_right():
        move()
        distance+=1
    return distance
def get_down(dist):
    while dist != 0:
        move()
        dist-=1

while True:
    distance = 0
    obstacle_check()
    if not wall_in_front() and not at_goal():
        move()
    if at_goal():
        break
"""

#another sol.
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()
def obstacle_check():
    if wall_in_front():
        turn_left()
        while wall_on_right():
            move()
        go_right()
        move()
        go_right()
        while front_is_clear():
            move()
        turn_left()
while not at_goal():
    if wall_in_front():
        obstacle_check()
    else:
        move()
"""

########################################
#final project 

#my sol.
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        go_right()
        move()
    elif front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_left()
"""

# other sols.
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        go_right()
        move()
    elif front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
"""
#########################
# best sol.
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        go_right()
        move()
    elif front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    elif wall_in_front():
        turn_left()
    

"""
###################
#another sol.
"""
import random
def go_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    var = random.randint(0,1)
    while front_is_clear() and right_is_clear():
        if var == 0:
            go_right()
            move()
        else:
            move()
    if right_is_clear():
        go_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""
###########################
#angela sol.
"""
def go_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        go_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""