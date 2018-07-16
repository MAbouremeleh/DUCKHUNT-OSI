import os, sys
import pygame
import config
import duckhunt
import registry
class Gun(object):
    def __init__(self, registry):
        self.registry = registry
        #num of bullets
        self.rounds = config.numRounds
        self.mousePos = (1,1) # Starting postion
        self.mouseImg = pygame.image.load(os.path.join('media', 'crosshairs.png'))

            #PEARDECK initialize self._joystick here
        self._joystick = pygame.joystick.Joystick(0)
        self._joystick.init()
        pygame.event.pump()
        pygame.event.get()


    def render(self):
        surface = self.registry.get('surface')
        surface.blit(self.mouseImg, self.mousePos)

    def reloadIt(self):
        #num of bullets per reload
        self.rounds = config.numReload

        # this method needs to return information about the state of the joystick PEARDECK
    def getJoystickPos(self):
        pygame.event.get()
        current_vert = int(self._joystick.get_axis(1)*1.5)
        current_horz = int(self._joystick.get_axis(0)*1.5)
        return current_horz, current_vert

    def neutralJoystick(self):
        return ((int(self._joystick.get_axis(0)*1.5) == 0) & ((int(self._joystick.get_axis(1)*1.5)) == 0))

    # method where you will want to use joystick inputs PEARDECK
    # initially get an idea of what the values currently being used for x,y,xoffset,yoffset are from the mouse -- print
        # run with old method, print values
    # mousePos = (x,y)
    def  moveCrossHairs(self):
        # xOffset = self.mouseImg.get_width() / 2
        # yOffset = self.mouseImg.get_height() / 2
        # x, y = pos
        pygame.event.get()
        y = int(self._joystick.get_axis(1)*1.5)
        x = int(self._joystick.get_axis(0)*1.5)
        #self.mousePos = (x - xOffset), (y - yOffset)
        # might have to put a ceiling and floor
        #f (self.mousePos[0] + (x*config.posSensitivity) > 500 | self.mousePos[0]  + (x*config.posSensitivity) < 0 ):
        #self.mousePos == self.mousePos 
        #elif (self.mousePos[1] + (y*config.posSensitivity) > 800 | self.mousePos[1] + (y*config.posSensitivity) < 0 ):
        #self.mousePos == self.mousePos
        if (self.mousePos[0] + (x*config.posSensitivity) < -25 ):
            self.mousePos = (- 15 ,self.mousePos[1])
        if (self.mousePos[0] + (x*config.posSensitivity) > (registry.ORIG_W - 25)):
            self.mousePos = ((registry.ORIG_W -35) ,self.mousePos[1])
        if (self.mousePos[1] + (y*config.posSensitivity) < -25 ):
            self.mousePos = ((self.mousePos[0]), -15)
        if (self.mousePos[1] + (y*config.posSensitivity) > (registry.ORIG_H- 25) ):
            self.mousePos = (self.mousePos[0],(registry.ORIG_H- 35))
        self.mousePos = ((self.mousePos[0] + x*config.posSensitivity ),(self.mousePos[1] + y*config.posSensitivity ))
       
        print ("POSITION: ", self.mousePos, (x,y))
        print(self._joystick.get_button(0))

    def isShooting(self):
        button = self._joystick.get_button(0)
        if button == 1:
            return True

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True

    