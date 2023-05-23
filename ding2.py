import requests
import json
from datetime import datetime
from datetime import date
import arabic_reshaper
from bidi.algorithm import get_display
 
#print(date.today())
def DING():
    try:
        z = {'api_token': '$2y$10$8DLW2hgCzgJoGNKPxn4YdevbmIfeMKGuUHJLTNefSF1nBzidwrooW',
             'from_date_time': '{} 00:00:00'.format(date.today())}

       
        response = requests.get('https://ws2.dingcenter.com/attendance/list',
                                params=z)

        x = response.json()
        xS = json.dumps(x)
        data = json.loads(xS)
        last_name = []
        NO = []
        TP = []
        AT = []
        DT = []
        for i in data:
            last_name.append(i['last_name'])
            NO.append(i['cell_number'])
            TP.append(i['type'])
            AT.append(i['action_type'])
            DT.append(i['date_time'])


        NO_INT = []

        for i in range(len(TP)):
            if TP[i] == 'in':
                NO_INT.append(1)
            else:
                NO_INT.append(0)
        bidi_text=[]
        for i in range(len(last_name)):
            reshaped_text = arabic_reshaper.reshape((last_name[i]))
            bidi_text.append (get_display(reshaped_text))
            #print(bidi_text)
        return [NO_INT, NO, bidi_text, DT]
    except:
        print('error')
#[NO_INT, NO, last_name, DT]=DING()

#print(NO_INT)



        
        
        