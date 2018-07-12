import os, sys
import pygame
import config
import duckhunt

class Gun(object):
    def __init__(self, registry):
        self.registry = registry
        #num of bullets
        self.rounds = config.numRounds
        self.mousePos = (0,0) # Starting postion
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


    # method where you will want to use joystick inputs PEARDECK
    # initially get an idea of what the values currently being used for x,y,xoffset,yoffset are from the mouse -- print
        # run with old method, print values
    # mousePos = (x,y)
    def moveCrossHairs(self, pos):
       # xOffset = self.mouseImg.get_width() / 2
       # yOffset = self.mouseImg.get_height() / 2
       # x, y = pos
       print ("POSITION")
       pygame.event.get()
       y = int(self._joystick.get_axis(1)*1.5)
       x = int(self._joystick.get_axis(0)*1.5)
        #self.mousePos = (x - xOffset), (y - yOffset)
        # might have to put a ceiling and floor
       self.mousePos = ((self.mousePos)[0] + x ), ((self.mousePos)[1] + y )
       print (self.mousePos)

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
