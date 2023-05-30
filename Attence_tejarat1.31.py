#import
from buRef import Button
import sys
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import pygame.freetype

import pygwidgets

from attencee import ALL
import arabic_reshaper
from bidi.algorithm import get_display
from pygame.locals import *
import datetime
import time



# making var as a global
global stringSETAD
global stringAIR
global stringJOLFA
global stringNorduz
global stringASTARA
global stringBILE
global p
global TIME_REF

#Button class
class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("BNazsanin.ttf", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        window.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="blue")
                    
                    global p
                    p=0


pygame.init()
window = pygame.display.set_mode((710, 560))

clock = pygame.time.Clock()
# 2 - Define constants
font = pygame.font.SysFont("BNazsanin.ttf", 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE=(245,110,20)

p=0
o=1

ft_font = pygame.freetype.SysFont('BNazsanin.ttf', 20)

background = pygame.Surface(window.get_size())

def TEXT_Manabe():
    ##jolfa
    J_X=30
    J_Y=20
      
    
    oMessageText1 = pygwidgets.DisplayText(window, (95,J_Y),'Jolfa', # Create a text object
                                    fontSize=36, textColor=ORANGE) # Set the font size and color
                                  
    oMessageText1.draw() # Draw the text object
  
    J_X=500 # Set the X coordinate of the text object
    J_Y=20 # Set the Y coordinate of the text object

    fon_S=15
    
    oMessageTextASTARA1 = pygwidgets.DisplayText(window, (500,J_Y),'ASTARA', 
                                    fontSize=36, textColor=ORANGE)
   
    oMessageTextASTARA1.draw()
   
    J_X=30
    J_Y=200
    oMessageText6 = pygwidgets.DisplayText(window, (80,J_Y),'NORDUZ', 
                                    fontSize=36, textColor=ORANGE)
  
    oMessageText6.draw()
    
    ##bil
    J_X=260
    J_Y=20
    oMessageText11 = pygwidgets.DisplayText(window, (J_X,J_Y),'BILESAVAR', 
                                    fontSize=36, textColor=ORANGE)
    
    oMessageText11.draw()
    
    ##AIRPORT
    J_X=500
    J_Y=200
    oMessageTextAT1 = pygwidgets.DisplayText(window, (J_X,J_Y),'AIRPORT', 
                                    fontSize=36, textColor=ORANGE)
   
    oMessageTextAT1.draw()
    oMessageTextASTARA9 = pygwidgets.DisplayText(window, (500,380),'SETAD', 
                                    fontSize=36, textColor=ORANGE)
    oMessageTextASTARA9.draw()
   
'''logoI=pygame.image.load('logo Tejarat_Arman.png').convert()

#logoIRECT=logoI.get_rect()
window.blit(logoI, (30,30))
'''
TEXTref="بارگذاری دوباره"
reshaped_text = arabic_reshaper.reshape(TEXTref)
refreshText= (get_display(reshaped_text))
button1 = Button(
    "restart",
    (280, 500),
    font=70,
    bg="blue",
    feedback="restart")
pygame.display.set_caption('Tejarat Electronic Arman Monitoring')

def handleError():
        TIME_REF=datetime.datetime.now()
        

                #TReturn =SE-time.time()
        [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell]=ALL()

                
        return [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell,TIME_REF]


            
    
run = True
while run:
    clock.tick(30)
    pygame. draw. polygon(window, (0,0,0), ((20,500),(20,560),(240,560),(240,500)))

    if p==0:
        [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell]=ALL()
        p=1
       
        TIME_REF= datetime.datetime.now()
        secTime=datetime.timedelta(0,300)+datetime.datetime.now()
    

                    
                    
    
    if datetime.datetime.now()>secTime:
        TIME_REF=datetime.datetime.now()
        [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell]=ALL()
        
        secTime=datetime.timedelta(0,300)+datetime.datetime.now()
    if NAME_BILE==0:
            TIME_REF=datetime.datetime.now()

           # time.sleep(10)
            [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell,TIME_REF]=handleError()
             

            
            
            


                  
    PMX=230
    PMY=180
    ###making polygon 
    pygame.draw.polygon(window,(0,68,255),((20,20),(230,20),(230,180),(20,180)))
    pygame.draw.polygon(window,(0,68,255),((20+PMX,20+PMY),(230+PMX,20+PMY),(230+PMX,180+PMY),(20+PMX,180+PMY)))
    pygame.draw.polygon(window,(0,68,255),((20,20+PMY),(230,20+PMY),(230,180+PMY),(20,180+PMY)))
    pygame.draw.polygon(window,(0,68,255),((20+PMX,20),(230+PMX,20),(230+PMX,180),(20+PMX,180)))
    
    pygame.draw.polygon(window,(0,68,255),((20+2*PMX,20),(230+2*PMX,20),(230+2*PMX,180),(20+2*PMX,180)))
    pygame.draw.polygon(window,(0,68,255),((20,20+2*PMY),(230,20+2*PMY),(230,180+2*PMY),(20,180+2*PMY)))

    pygame.draw.polygon(window,(0,68,255),((20+2*PMX,20+2*PMY),(230+2*PMX,20+2*PMY),(230+2*PMX,180+2*PMY),
                                           (20+2*PMX,180+2*PMY)))

    pygame.draw.polygon(window,(0,68,255),((20+2*PMX,20+PMY),(230+2*PMX,20+PMY),(230+2*PMX,180+PMY),
                                           (20+2*PMX,180+PMY)))
    
    #show the background and Text
    TEXT_Manabe()
    J_X=160
    J_Y=-50
    S_F=30
    
    oMessageText105 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='BNazsanin.ttf',value=NAME_UK_jolfa, 
                                    fontSize=S_F, textColor=WHITE)
   
    oMessageText105.draw()
    
    #### text norduz
    J_X=160
    J_Y=100
    
    oMessageTextN4 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='BNazsanin.ttf',value=NAME_UK_norduz, 
                                    fontSize=S_F, textColor=WHITE)
    
    oMessageTextN4.draw()
    #bil
    J_X=380
    J_Y=-50
   
    oMessageTextB5 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='BNazsanin.ttf',value=NAME_UK_BILE, 
                                    fontSize=S_F, textColor=WHITE)
  
    oMessageTextB5.draw()

    ## airport
    
    J_X=600
    J_Y=100

    oMessageTextAP5 = pygwidgets.DisplayText(window, (J_X-70, J_Y+150),fontName='BNazsanin.ttf',value= NAME_UK_AIR, 
                                    fontSize=S_F, textColor=WHITE)
    
    oMessageTextAP5.draw()
    
    ## ASTARAA
    J_X=630
    J_Y=-50   

    oMessageTextAP5 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='BNazsanin.ttf',value=NAME_UK_ASTARA, 
                                    fontSize=S_F, textColor=WHITE)

    oMessageTextAP5.draw()
    
    ###ALLLL
    J_X=600
    J_Y=380
    
    oMessageTextX = pygwidgets.DisplayText(window, (J_X, J_Y),fontName='BNazsanin.ttf',value=(stringSETAD), 
                                    fontSize=16, textColor=WHITE)
    
    oMessageTextX.draw()
  
    oMessageTextref = pygwidgets.DisplayText(window, (20, J_Y+160),fontName='BNazsanin.ttf',value=TIME_REF, 
                                    fontSize=15, textColor=WHITE)
    
    oMessageTextref.draw()
   
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()
            button1.click(event)
            button1.show()