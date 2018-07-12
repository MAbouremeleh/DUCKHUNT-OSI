import pygame
import sys
import time
pygame.init()
pygame.joystick.init()

print (pygame.joystick.get_count())

_joystick = pygame.joystick.Joystick(0)
_joystick.init()
pygame.event.pump()
print (_joystick.get_init())
print (_joystick.get_id())
print (_joystick.get_name())
print("axis")
print (_joystick.get_numaxes())
print (_joystick.get_numballs())
print("num buttons: ")
print (_joystick.get_numbuttons()) #12

print (_joystick.get_numhats())
print()

pygame.event.get()
up_init = int(_joystick.get_axis(1)) #Initalizing up joystick postion
left_init = int(_joystick.get_axis(0)) #Intializing left joystick postion
right_init = (_joystick.get_axis(2)) # Initializing right joystick position
down_init = (_joystick.get_axis(3)) #Initialzing down joystick position

print(up_init)
print(left_init)
print(down_init)
print(right_init)
'''
while True:
    current_up = int(_joystick.get_axis(1))
    current_left = int(_joystick.get_axis(0))
    current_right = (_joystick.get_axis(2))
    current_down = (_joystick.get_axis(3))
    if  current_up != up_init:
        print("up") #Vert =-1 means Up
        print (current_up)
    elif  current_left != left_init:
        print("left") #Horz =-1 means Left
        print (current_left)
    elif current_right != right_init:
        print("right")
        print (current_right)
    elif current_down != right_init:
        print("down")
        print (current_down)
    else:
        print("else")
        #print(current_up)
        #print(current_left)
        print(current_right)
        #print(current_down)
        
    (pygame.event.get())
        '''