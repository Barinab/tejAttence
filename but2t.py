from pygame.locals import *
import pygame
import sys
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
ORANGE=(245,110,20)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BALL_WIDTH_HEIGHT = 100
RED=(255,0,0)

class SimpleButton():
    STATE_IDLE ='idle'
    STATE_ARMED='armed'
    STATE_DISARMED='disarmed'
    def __init__(self,window,loc,up,down) :
        self.window=window
        self.loc=loc
        self.surfaceUp=pygame.image.load(up)
        self.surfaceDown=pygame.image.load(down)
        
        
        self.rect=self.surfaceUp.get_rect()
        self.rect[0]=loc[0]
        self.rect[1]=loc[1]
        
        self.state=SimpleButton.STATE_IDLE
    def handleEvent(self,eventObj):
        if eventObj.type not in (MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN):
            return False
        eventPointInButtonRect=self.rect.collidepoint(eventObj.pos)
        if self.state==SimpleButton.STATE_IDLE:
            if(eventObj.type==MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state=SimpleButton.STATE_ARMED
            elif self.state == SimpleButton.STATE_ARMED:
                if (eventObj.type ==MOUSEBUTTONUP) and eventPointInButtonRect:
                    self.state=SimpleButton.STATE_IDLE
                    return True
            if (eventObj.type==MOUSEMOTION) and(not eventPointInButtonRect):
                self.state =SimpleButton.STATE_DISARMED
            elif self.state == SimpleButton.STATE_DISARMED:
                if eventPointInButtonRect:
                    self.state=SimpleButton.STATE_ARMED
                elif eventObj.type==MOUSEBUTTONUP:
                    self.state=SimpleButton.STATE_IDLE
                return False
    def draw(self):
        if self.state==SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown,self.loc)
        else:
            self.window.blit(self.surfaceUp,self.loc)
pygame.init()
window = pygame.display.set_mode((800, 600))
oButton = SimpleButton(window, (150, 30),'images/buttonUp.png','images/buttonDown.png')
# 6 - Loop forever
while True:
# 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    if oButton.handleEvent(event):
        print('User has clicked the button')
    window.fill(GRAY)
    oButton.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
    