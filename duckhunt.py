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
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key is 27):
            self.running = False
        else:
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
        while (self.running):
            #repeat = True
            #while(repeat):
            
            for event in pygame.event.get():
               # type = 2
#                print("event.dict.values()[1]: ", event.dict.values()[1])
                if ((event.type == pygame.JOYAXISMOTION)):
                    # & event.type == 2):
                    # change to be the joystick var -- 2 is keydown
                    config.JSMOVEMENT = True
                    # pygame.event.clear()
                    pygame.event.post(event)
                    print("adding event to queue")
                #print("event type, key value, counter: ", event.type, event.dict.values()[1], config.COUNTER)
                #config.COUNTER += 1
                # print(event.key)
                self.handleEvent(event)

                # does the event change when going back to neutral position?
                # if so, when that happens change config back to false
                if (config.JSMOVEMENT):
                    config.JSMOVEMENT = False
                else:
                    pygame.event.clear()
                    #break

                '''
                print ("HERE")
               print("type")
                print(pygame.JOYAXISMOTION)
                print(type)
                # type = 2
                #print("event.dict.values()[1]: ", (type))
                if (~(self.neutralJoystick())):
                    print("in and")
                    # & event.type == 2):
                    # change to be the joystick var -- 2 is keydown
                    config.JSMOVEMENT = True
                    # pygame.event.clear()
                    pygame.event.post(event)
                #print("event type, key value, counter: ", event.type, event.dict.values()[1], config.COUNTER)
                config.COUNTER += 1
                # print(event.key)
                self.handleEvent(event)

                # does the event change when going back to neutral position?
                # if so, when that happens change config back to false
                if (config.JSMOVEMENT):
                    config.JSMOVEMENT = False
                    print ("resetting")
                else:
                    pygame.event.clear()
                    break
                
                
 
                    print("PEACH:")
                #while((pygame.event.get().type == pygame.JOYAXISMOTION)):
                    self.handleEvent(event)
                    if(event.type != pygame.JOYAXISMOTION):
                        repeat = False
                        
                        '''

            self.loop()
            self.render()
        
        self.cleanup()

if __name__ == "__main__":
    theGame = Game()
    theGame.execute()