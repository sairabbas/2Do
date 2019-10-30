from datetime import datetime, date, time
import calendar, re, datetime

#this function for converting the input form of HTML to DB 
def transformForm(deadline):
        n= re.split("[- : T]", deadline)
        array = ['Y','M','D','H','Min']
        dict={}
        for i in range (len(n)):
             dict.update({array[i] : n[i]})
        mm = dict['M']

        #change the month "word" to  the month "number"
        dict1 = {}
        for mw, mn in enumerate(calendar.month_abbr):
            dict1.update({ mw : mn })
        for mw, mn  in dict1.items():
            if mm == mn:
                mm = mw
        dict['M'] = mm
        deadline = datetime.datetime(int(dict['Y']),int(dict['M']),int(dict['D']),int(dict['H']),int(dict['Min']))
        return deadline
