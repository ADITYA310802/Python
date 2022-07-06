
"""
#build_wall()
turn_around()
#turn_left()
move()
move()
turn_right()
move()
turn_left()
move()
move()
turn_left()
move()
move()
turn_right()
move()
move()
turn_right()
move()
move()
#hurdle
def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()"""

#final maze:

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while front_is_clear():
    move()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            
       
        
    
     
        
    
    


