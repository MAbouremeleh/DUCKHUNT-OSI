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
vert_init = int(_joystick.get_axis(1)) #Initalizing up joystick postion
horz_init = int(_joystick.get_axis(0)) #Intializing left joystick postion


print(vert_init)
print(horz_init)
while True:
    current_vert = int(_joystick.get_axis(1)*1.5)
    current_horz = int(_joystick.get_axis(0)*1.5)
    if  current_vert != vert_init:
        print("vert") #Vert =-1 means Up
        print (current_vert)
    elif  current_horz != horz_init:
        print("horz") #Horz =-1 means Left
        print (current_horz)
    else:
        print("else")
        print(current_vert)
        print(current_horz)
        
    (pygame.event.get())