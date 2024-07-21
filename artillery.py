#!/usr/bin/env python

from math import *
import random, time

#=======================================================================
#                        FUNCTION AREA
#=======================================================================
def calc_range(vel,angle, gravity):
    """Calulate the range of a projectile given the angle in radians and
    the velocity in m/s """
    return (2*(vel**2)*sin(angle)*cos(angle))/gravity
   
def end_game():
    for y in range(0,5):
        for x in range(0,20):
            print (" "*x,"YOU HIT THE TARGET!!")
            time.sleep(.03)
        for x in range(20,-1,-1):
            print (" "*x,"YOU HIT THE TARGET!!")
            time.sleep(.03)

def reset_game():
    global gravity, vel, target_distance, game_over, num_tries
    global error_margin
    gravity = random.uniform (1.0,25.0)
    vel = random.randint(50,350)
    target_distance = random.randint(100, int(calc_range(vel,45, gravity) ))
    game_over = False
    num_tries = 0 
    choice = -1
    while(choice <1 or choice>len(difficulty_list) ):
        print ("""
1 = Very easy
2 = Easy
3 = Moderate
4 = Hard
5 = Very hard
""")

        choice = int (input("Enter the difficulty level: "))
    error_margin = difficulty_list[choice-1]

    
def instructions():
    print ("""
                    ARTILLERY!!!
             
This is the game of artillery!  You must hit a target with your artillery 
gun given a fixed muzzle velocity.  You will initially be asked for a 
difficulty level from 1-4 with 1 being the hardest and 4 being the easiest:

1 = Very easy
2 = Easy
3 = Moderate
4 = Hard
5 = Very hard

Each round you will be asked to input your gun elevation in degrees. 
You may eneter an integer or floating point number from 0 to 90 degrees.
You will then be told if you hit the target or missed and by how much.

    """)

#=======================================================================
#                        GLOBAL VARIABLE AREA
#=======================================================================
error_margin = None
gravity = None
vel = None
target_distance = None
game_over = False
num_tries = None
difficulty_list = [30, 20, 10, 5, 1 ]

def print_header():
    print ("\n============================")
    print ("Shot #:",num_tries+1)
    print ("Muzzle velocity:",vel,"m/s.")
    print ("Gravity: %.2f m/s*s" %(gravity))
    print ("Distance to target:", target_distance,"meters")
    print ("You must hit within", error_margin,"meters of your target.")

instructions()
reset_game()

#=======================================================================
#                        MAIN GAME LOOP
#=======================================================================
while(game_over == False):
    print_header()
    
    angle = -1
    while(angle < 0 or angle > 90):
        angle = float (input("Firing angle: ") )
    angle = radians(angle)
    shot_distance = int(calc_range(vel, angle, gravity))

    if (shot_distance < target_distance-error_margin):
        print ("You undershot the target by", target_distance-shot_distance,"meters.")
        num_tries +=1
    elif (shot_distance > target_distance+error_margin):
        print ("You overshot the target by", shot_distance-target_distance,"meters.")
        num_tries+=1
    else:
        num_tries+=1
        end_game()
        print ("\n\n**You got it in",num_tries,"tries!**")
        again = input("Play again (Y/N): ")
        if again == "n" or again == "N":
            game_over = True
        else:
            reset_game() 
            
