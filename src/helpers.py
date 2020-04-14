import re
import configparser
import json
#Normalises days
def timenormaliseday(periodType,timeToElapse):
  # timevalue
    # timevalue=line.rstrip()
    daysen=re.findall(r'\d+', periodType)
    dayvalue=0
    if periodType=="days" or periodType=="day":
       dayvalue=timeToElapse
    elif len(daysen)== 0:
       dayvalue=0
    elif periodType=="weeks" or periodType=="week" and len(daysen)!= 0:
       dayvalue=timeToElapse*7 #convert weeks to days 
    elif periodType=="month" or periodType=="months" and len(daysen)!= 0:
       dayvalue=timeToElapse*30 #convert month to days assuming the standard months are 30 
    return dayvalue

#Read Settings Files
def read_config():
    config = configparser.ConfigParser()
    config.read('app.properties')
    print("Njovu")
    return config.sections()
   #  try:
   #      json.loads(jsonData)
   #      return True
   #  except ValueError as err:
   #      return False