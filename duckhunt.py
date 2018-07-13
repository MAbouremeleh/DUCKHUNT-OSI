import os, sys
import config
import pygame
import pygame.transform
import states
from game.registry import adjpos, adjrect, adjwidth, adjheight
from game.gun import Gun

# Game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = adjpos (800, 500)
TITLE = "Symons Media: Duck Hunt"
FRAMES_PER_SEC = config.frames

BG_COLOR = 255, 255, 255

# Initialize pygame before importing modules
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.display.set_caption(TITLE)
pygame.mouse.set_visible(False)

import game.driver
#from game.states import BaseState

class Game(object):
    def __init__(self):
        self.running = True
        self.surface = None
        self.clock = pygame.time.Clock()
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT

       

        background = os.path.join('media', 'background.jpg')
        bg = pygame.image.load(background)
        self.size = (int(self.size[0]), int(self.size[1]))
        self.background = pygame.transform.smoothscale (bg, self.size)
        self.driver = None

    def init(self):
        self.surface = pygame.display.set_mode(self.size)
        self.driver = game.driver.Driver(self.surface)
        pygame.joystick.init()

    def handleEvent(self, event):
        print("shark")
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key is 27):
            self.running = False
            print("koala")
        else:
            print("kangaroo")
            self.driver.handleEvent(event)

    def loop(self):
        self.clock.tick(FRAMES_PER_SEC)
        self.driver.update()

    def render(self):
        self.surface.blit(self.background, (0,0))
        self.driver.render()
        #self.PlayState.crosshairs()
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
        sys.exit(0)

    def execute(self): 
        self.init()
        print("apple")
        while (self.running):
            
            for event in pygame.event.get():
            #while((pygame.event.get().type == pygame.JOYAXISMOTION)):
                print("peach")
                self.handleEvent(event)
            self.loop()
            self.render()

        self.cleanup()

if __name__ == "__main__":
    theGame = Game()
    theGame.execute()
