#hozur ghiab
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
from ding2 import DING
from datetime import datetime
from datetime import date

def ALL():
    try:
        # time.sleep(5)
       # global stringJOLFA, stringJOLFA_FA

        [VAZ, NO, last_name, datemarz] = DING()
        jolfa_hazery = []
        jolfa_hazery_FA = []
        jolfa_tell=[]

        tell_jolfa = [989143919834, 989143921126,
                      989148277712, 989149910396, 989145787155]
        #esmaye_jolfa = ['Afshari', 'Sadeghy', 'Asghari', 'Jaberi', 'Azimi']

        CORECTDATE = []

        for i in range(len(datemarz)-1):
            CORECTDATE.append(datetime.strptime(
                datemarz[i+1], '%Y-%m-%d %H:%M:%S'))

        for X in range(0,5):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])==tell_jolfa[X]:
                    if VAZ[J]==1:
                        jolfa_hazery.append(last_name[J])
                        jolfa_hazery_FA.append(last_name[J])
                        jolfa_tell.append(str(NO[J]))
                        
                    break
        Mylist_jolfa = list(dict.fromkeys(jolfa_hazery))
       # Mylist_jolfa_FA = list(dict.fromkeys(jolfa_hazery_FA))
        #stringJOLFA = ','.join(Mylist_jolfa)
        #stringJOLFA_FA = ','.join(Mylist_jolfa_FA)
        
        Mylist_jolfa_tell = list(dict.fromkeys(jolfa_tell))
        #stringJOLFA_tell = ','.join(Mylist_jolfa_tell)
        stringJOLFA=Mylist_jolfa

        stringJOLFA_tell=Mylist_jolfa_tell
        





# norduz
#        global stringNorduz, stringNorduz_FA

        norduz_hazery = []
        norduz_hazery_FA = []
        norduz_tell=[]

        tell_norduz = [989030989197, 989148867748,
                   989145729504, 989332404134]
        #esmaye_norduz = ['HasanNezhad', 'SALEHI', 'Aali', 'Alipour']
        CORECTDATE = []

       

        for X in range(0,4):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])==tell_norduz[X]:
                    if VAZ[J]==1:
                        norduz_hazery.append(last_name[J])
                        norduz_hazery_FA.append(last_name[J])
                        norduz_tell.append(str(NO[J]))
                    break
        Mylist_norduz = list(dict.fromkeys(norduz_hazery))
        Mylist_norduz_FA = list(dict.fromkeys(norduz_hazery_FA))

        stringNorduz = ','.join(Mylist_norduz)
        stringNorduz_FA = ','.join(Mylist_norduz_FA)
        
        
        Mylist_nurduz_tell = list(dict.fromkeys(norduz_tell))
        #stringnoruz_tell = ','.join(Mylist_nurduz_tell)

        stringNorduz=Mylist_norduz
        stringnoruz_tell=Mylist_nurduz_tell

#        global stringAIR, stringAIR_FA

        AIR_hazery = []
        AIR_hazery_FA = []
        AIR_tell=[]

        tell_AIR = [989334789356, 989307594802,
                989389728997, 989390648966]
        esmaye_AIR = ['Ghamarpoor', 'Ghamgosar', 'Ghafarpour', 'Gheytasi']
        CORECTDATE = []

        

        for X in range(0,4):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])==tell_AIR[X]:
                    if VAZ[J]==1:
                        AIR_hazery.append(last_name[J])
                        AIR_hazery_FA.append(last_name[J])
                        AIR_tell.append(str(NO[J]))
                    break
        Mylist_AIR = list(dict.fromkeys(AIR_hazery))
        #stringAIR = ','.join(Mylist_AIR)
        #Mylist_AIR_FA = list(dict.fromkeys(AIR_hazery_FA))

        #stringAIR_FA = ','.join(Mylist_AIR_FA)
        
        
        Mylist_AIR_tell = list(dict.fromkeys(AIR_tell))
        #stringAIR_tell = ','.join(Mylist_AIR_tell)


        stringAIR=Mylist_AIR
        stringAIR_tell=Mylist_AIR_tell

   
        global stringASTARA, stringASTARA_FA

        ASTARA_hazery = []
        ASTARA_hazery_FA = []
        ASTARA_tell=[]

        tell_ASTARA = [989114706033, 989014511072]
        esmaye_ASTARA = ['Satarpour', 'Akbarnia']
        CORECTDATE = []

       

        for X in range(0,2):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])==tell_ASTARA[X]:
                    if VAZ[J]==1:
                        ASTARA_hazery.append(last_name[J])
                        ASTARA_hazery_FA.append(last_name[J])
                        ASTARA_tell.append(str(NO[J]))
                    break
        Mylist_ASTARA = list(dict.fromkeys(ASTARA_hazery))

        #Mylist_ASTARA_FA = list(dict.fromkeys(ASTARA_hazery_FA))
        #stringASTARA = ','.join(Mylist_ASTARA)
        #stringASTARA_FA = ','.join(Mylist_ASTARA_FA)
        
        Mylist_ASTARA_tell = list(dict.fromkeys(ASTARA_tell))
        #stringASTARA_tell = ','.join(Mylist_ASTARA_tell)


        stringASTARA=Mylist_ASTARA
        stringASTARA_tell=Mylist_ASTARA_tell



        global stringBILE, stringBILE_FA

        BILE_hazery = []
        BILE_hazery_FA = []
        BILE_tell=[]
        

        tell_BILE = [989149559282, 989383008763, 989144513155]
        esmaye_BILE = ['Babai', 'Hekmati', 'Mohsenpour']

        CORECTDATE = []

        
        for X in range(0,3):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])==tell_BILE[X]:
                    if VAZ[J]==1:
                        BILE_hazery.append(last_name[J])
                        BILE_hazery_FA.append(last_name[J])
                        BILE_tell.append(str(NO[J]))
                    break
        #Mylist_BILE_FA = list(dict.fromkeys(BILE_hazery_FA))
        Mylist_BILE = list(dict.fromkeys(BILE_hazery))
        #stringBILE = ','.join(Mylist_BILE)
        #stringBILE_FA = ','.join(Mylist_BILE_FA)
        
        Mylist_bile_tell = list(dict.fromkeys(BILE_tell))
        #stringbile_tell = ','.join(Mylist_bile_tell)

        stringBILE=Mylist_BILE
        stringbile_tell=Mylist_bile_tell

    
        global stringSETAD, stringSETAED_FA

        Setad_hazery = []
        Setad_hazery_FA = []
        Setad_tell=[]

        tell_SETAD = [989121965648, 989153356025,989129570217,989334671830,989126446118,989192160935 ,  \
            989021174799,989386929289,989100831816, 989124238759, 989198182042, 989128588299, 989018391363]
        esmaye_SETAD = ['Bayanian', 'Mohammadian','Sadeghi','Jafarkhani', \
            'Fahami','Roshan','Meliani','Abri','Ahmadi','Jahani','Baradari','Heydarian','ARMAN TEST']
        
        

        CORECTDATE = []

        
        for X in range(len(tell_SETAD)):

            for J in range(len(NO)-1,0,-1):
                if int(NO[J])== tell_SETAD[X]:
                    if VAZ[J]==1:
                        Setad_hazery.append(last_name[J])
                        Setad_hazery_FA.append(last_name[J])
                        Setad_tell.append(str(NO[J]))
                    break
        Mylist_SETAD = list(dict.fromkeys(Setad_hazery))
        #stringSETAD = ','.join(Mylist_SETAD)
        #stringSETAD_FA = ','.join(Setad_hazery_FA)
        
        Mylist_SETAD_tell = list(dict.fromkeys(Setad_tell))
        #stringSETAD_tell = ','.join(Mylist_SETAD_tell)
        stringSETAD=Mylist_SETAD
        stringSETAD_tell=Mylist_SETAD_tell
        
        return [stringJOLFA, stringJOLFA_tell, stringNorduz, stringnoruz_tell, stringAIR, stringAIR_tell, stringASTARA, stringASTARA_tell, stringBILE, stringbile_tell,stringSETAD,stringSETAD_tell]

    except:
        stringJOLFA = -100
        stringJOLFA_tell = -100
        stringNorduz = -100
        stringnoruz_tell = -100
        stringAIR = -100
        stringAIR_tell = -100
        stringASTARA = -100
        stringASTARA_tell = -100
        stringBILE = -100
        stringbile_tell = -100
        stringSETAD=-100
        stringSETAD_tell=-100
        
        return [stringJOLFA, stringJOLFA_tell, stringNorduz, stringnoruz_tell, stringAIR, stringAIR_tell, stringASTARA, stringASTARA_tell, stringBILE, stringbile_tell,stringSETAD,stringSETAD_tell]



#[stringJOLFA, stringJOLFA_tell, stringNorduz, stringnoruz_tell, stringAIR, stringAIR_tell, stringASTARA, stringASTARA_tell, stringBILE, stringbile_tell,stringSETAD,stringSETAD_tell]=ALL()
    

#print(stringSETAD)
