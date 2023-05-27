#hozur ghiab
from buRef import Button
import sys
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import pygame.freetype
#import testding_2py
#import schedule
import pygwidgets
import time
#import Cal_borders
#import TEDAD_RUZ
from attencee import ALL
import arabic_reshaper
from bidi.algorithm import get_display
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
global p 
p=0
global stringSETAD
global stringAIR
class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
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
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="blue")
                    
                    global p
                    p=0
                    #print(p)
                    '''[stringJOLFA, stringJOLFA_tell, stringNorduz, stringnoruz_tell, stringAIR, stringAIR_tell, stringASTARA, 
                     stringASTARA_tell, stringBILE, stringbile_tell,stringSETAD,stringSETAD_tell] =ALL()'''
                    #print(stringSETAD)



'''def calling_ding():
    return [stringJOLFA, stringJOLFA_tell, stringNorduz, stringnoruz_tell, stringAIR, stringAIR_tell, stringASTARA, stringASTARA_tell, stringBILE, stringbile_tell,stringSETAD,stringSETAD_tell]
'''
        



    
pygame.init()
window = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
# 2 - Define constants
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

ft_font = pygame.freetype.SysFont('Times New Roman', 20)

background = pygame.Surface(window.get_size())

#schedule.every(1).minutes.do(ty)
#schedule.every(1).minutes.do(ADADAYE_MARZA)

o=1

def TEXT_Manabe():
    ##jolfa
    J_X=30
    J_Y=20
    fon_S=15
    
    
    oMessageText1 = pygwidgets.DisplayText(window, (95,J_Y),'Jolfa', 
                                    fontSize=36, textColor=ORANGE)
    '''
    oMessageText2 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText3 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText4 = pygwidgets.DisplayText(window, (J_X, J_Y+100),'CANCEL by Admin', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText5 = pygwidgets.DisplayText(window, (J_X, J_Y+130),'CANCEL by SYSTEM', 
                                    fontSize=fon_S, textColor=WHITE)
                                    '''
    oMessageText1.draw()
    #oMessageText2.draw()
    #oMessageText3.draw()
    #oMessageText4.draw()
    #oMessageText5.draw()
    
    ###ASTARA
    J_X=500
    J_Y=20
    fon_S=15
    
    
    oMessageTextASTARA1 = pygwidgets.DisplayText(window, (500,J_Y),'ASTARA', 
                                    fontSize=36, textColor=ORANGE)
    '''oMessageTextASTARA2 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextASTARA3 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextASTARA4 = pygwidgets.DisplayText(window, (J_X, J_Y+100),'CANCEL by Admin', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextASTARA5 = pygwidgets.DisplayText(window, (J_X, J_Y+130),'CANCEL by SYSTEM', 
                                    fontSize=fon_S, textColor=WHITE)'''
    oMessageTextASTARA1.draw()
    #oMessageTextASTARA2.draw()
    #oMessageTextASTARA3.draw()
    #oMessageTextASTARA4.draw()
    #oMessageTextASTARA5.draw()
    
    ##norduz
    J_X=30
    J_Y=200
    oMessageText6 = pygwidgets.DisplayText(window, (80,J_Y),'NORDUZ', 
                                    fontSize=36, textColor=ORANGE)
    '''oMessageText7 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText8 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText9 = pygwidgets.DisplayText(window, (J_X, J_Y+100),'CANCEL by Admin', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText10 = pygwidgets.DisplayText(window, (J_X, J_Y+130),'CANCEL by SYSTEM', 
                                    fontSize=fon_S, textColor=WHITE)'''
    #oMessageText10.draw()
    #oMessageText9.draw()
    #oMessageText8.draw()
    #oMessageText7.draw()
    oMessageText6.draw()
    
    ##bil
    J_X=260
    J_Y=20
    oMessageText11 = pygwidgets.DisplayText(window, (J_X,J_Y),'BILESAVAR', 
                                    fontSize=36, textColor=ORANGE)
    '''oMessageText12 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText13 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText14 = pygwidgets.DisplayText(window, (J_X, J_Y+100),'CANCEL by Admin', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageText15 = pygwidgets.DisplayText(window, (J_X, J_Y+130),'CANCEL by SYSTEM', 
                                    fontSize=fon_S, textColor=WHITE)'''
    oMessageText11.draw()
    #oMessageText12.draw()
    #oMessageText13.draw()
    #oMessageText14.draw()
    #oMessageText15.draw()
    
    
    
    
    ##AIRPORT
    J_X=500
    J_Y=200
    oMessageTextAT1 = pygwidgets.DisplayText(window, (J_X,J_Y),'AIRPORT', 
                                    fontSize=36, textColor=ORANGE)
    '''oMessageTextAT2 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextAT3 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextAT4 = pygwidgets.DisplayText(window, (J_X, J_Y+100),'CANCEL by Admin', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextAT5 = pygwidgets.DisplayText(window, (J_X, J_Y+130),'CANCEL by SYSTEM', 
                                    fontSize=fon_S, textColor=WHITE)'''
    oMessageTextAT1.draw()
    oMessageTextASTARA9 = pygwidgets.DisplayText(window, (500,380),'SETAD', 
                                    fontSize=36, textColor=ORANGE)
    oMessageTextASTARA9.draw()
    #oMessageTextAT2.draw()
    #oMessageTextAT3.draw()
    #oMessageTextAT4.draw()
    #oMessageTextAT5.draw()
    
    '''
    ####hame marzha
    J_X=500
    J_Y=390
    
    oMessageTextA1 = pygwidgets.DisplayText(window, (J_X,J_Y),'ALL', 
                                    fontSize=36, textColor=ORANGE)
    oMessageTextA2 = pygwidgets.DisplayText(window, (J_X, J_Y+40),'NO. Per DAY', 
                                    fontSize=fon_S, textColor=WHITE)
    oMessageTextA3 = pygwidgets.DisplayText(window, (J_X, J_Y+70),'NO. Per Month', 
                                    fontSize=fon_S, textColor=WHITE)'''
    
    #oMessageTextA1.draw()
    #oMessageTextA2.draw()
    #oMessageTextA3.draw()
    #text_rect = ft_font.get_rect('ty()')
    #text_rect.center = window.get_rect().center
    #ft_font.render_to(window, text_rect.topleft, str(jolfa_PD), (255, 0, 0))
#schedule.every(1).minutes.do(text_ADAD)
'''logoI=pygame.image.load('logo Tejarat_Arman.png').convert()

#logoIRECT=logoI.get_rect()
window.blit(logoI, (30,30))
'''

button1 = Button(
    "REFRESH",
    (280, 500),
    font=30,
    bg="blue",
    feedback="REFRESH")
run = True
pygame.display.set_caption('Tejarat Electronic Arman Monitoring')
if p==0:
    
    [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell]=ALL()
    p=1
while run:
    clock.tick(30)
    
    if p==0:
        [NAME_UK_jolfa, NAME_jolfa,NAME_UK_norduz, NAME_norduz, NAME_UK_AIR, NAME_AIR,NAME_UK_ASTARA, NAME_ASTARA,NAME_UK_BILE, NAME_BILE,stringSETAD,stringSETAD_tell]=ALL()
        p=1
        #print(stringSETAD,NAME_UK_AIR)
            
   
    PMX=230
    PMY=180
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
    ##window.blit(logoI, (20+PMX+30,180+PMY+40))

    TEXT_Manabe()
    J_X=160
    J_Y=-50
    S_F=30
    ##
    
    #[NAME_UK_jolfa, NAME_jolfa]=testding_2py.JOLFA()
    
    #print(stringSETAD)
    ##jolfa
    
    oMessageText105 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='bZb.ttf',value=NAME_UK_jolfa, 
                                    fontSize=S_F, textColor=WHITE)
   
    oMessageText105.draw()

    
    #### text norduz
    J_X=160
    J_Y=100
  
    
    #[NAME_UK_norduz, NAME_norduz]=testding_2py.norduz()

    oMessageTextN4 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='bZb.ttf',value=NAME_UK_norduz, 
                                    fontSize=S_F, textColor=WHITE)
    #print(NAME_UK_norduz)
    
    oMessageTextN4.draw()
    #bil
    J_X=380
    J_Y=-50
   
    
    
    
    #[NAME_UK_BILE, NAME_BILE]=testding_2py.BILE()

    oMessageTextB5 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='bZb.ttf',value=NAME_UK_BILE, 
                                    fontSize=S_F, textColor=WHITE)
  
    oMessageTextB5.draw()

    ## airport
    
    J_X=600
    J_Y=100
    
    
    #[NAME_UK_AIR, NAME_AIR]=testding_2py.AIR()

    oMessageTextAP5 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='bZb.ttf',value= NAME_UK_AIR, 
                                    fontSize=S_F, textColor=WHITE)
    
    oMessageTextAP5.draw()

    
    ## ASTARAA
    J_X=630
    J_Y=-50
    
   
    #[NAME_UK_AIR, NAME_AIR]=testding_2py.ASTARA()

    oMessageTextAP5 = pygwidgets.DisplayText(window, (J_X-80, J_Y+150),fontName='bZb.ttf',value=NAME_UK_ASTARA, 
                                    fontSize=S_F, textColor=WHITE)
    
  
    oMessageTextAP5.draw()

    #print(len(stringSETAD))
    
    ###ALLLL
    J_X=550
    J_Y=400
    
    oMessageTextX = pygwidgets.DisplayText(window, (J_X, J_Y),fontName='bZb.ttf',value=(stringSETAD), 
                                    fontSize=17, textColor=WHITE)
    #oMessageTextY = pygwidgets.DisplayText(window, (J_X, J_Y+70),stringSETAD, 
     #                               fontSize=S_F, textColor=WHITE)
    
    oMessageTextX.draw()
    #oMessageTextY.draw()
  

   
    
    pygame.display.flip()
    #schedule.run_pending()
    #time.sleep(10)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()
            
            button1.click(event)

            button1.show()
