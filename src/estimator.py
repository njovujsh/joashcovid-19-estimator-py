import json
import sys
from src.helpers import timenormaliseday


data_jsonx =  '{"region":{"name":"Africa","avgAge":19.7,"avgDailyIncomeInUSD":5,"avgDailyIncomePopulation":0.71}, "periodType":"days","timeToElapse":58,"reportedCases":674,"population":66622705,"totalHospitalBeds":1380614}'

def estimator(data):
#   data=json.loads(data)
  reportedCases=data["reportedCases"]
  impact= {
  'data':data, #the input data you got
  'impact':{'currentlyInfected':reportedCases*10}, #your best case estimation,
  'severeImpact':{'currentlyInfected':reportedCases*50} #your severe case estimationl,
  }
#   impact["estimate"]["impact"]["currentlyInfected"]=1
  factor=int(timenormaliseday(data['periodType'],data['timeToElapse'])*1/3)
  # Edited output by number of days per infected people
  #Challenge 1
  impact['impact']['infectionsByRequestedTime']=impact['impact']['currentlyInfected']*(2**factor)
  impact['severeImpact']['infectionsByRequestedTime']=impact['severeImpact']['currentlyInfected']*(2**factor)

  #severe cases by requested time  
  impact['impact']['severeCasesByRequestedTime']=int(impact['impact']['infectionsByRequestedTime']*(15/100))
  impact['severeImpact']['severeCasesByRequestedTime']=int(impact['severeImpact']['infectionsByRequestedTime']*(15/100))

  #hospital beds by requested time
  expectedtotalHospitalBeds=int(data["totalHospitalBeds"]*(35/100)) #Assumption is 1 bed per person
  impact['impact']['hospitalBedsByRequestedTime']=expectedtotalHospitalBeds-impact['impact']['severeCasesByRequestedTime']
  impact['severeImpact']['hospitalBedsByRequestedTime']=expectedtotalHospitalBeds-impact['severeImpact']['severeCasesByRequestedTime']

  #estimated number of severe positive cases that will require ICU care.
  impact['impact']['casesForICUByRequestedTime']=int(impact['impact']['infectionsByRequestedTime']*(5/100))
  impact['severeImpact']['casesForICUByRequestedTime']=int(impact['severeImpact']['infectionsByRequestedTime']*(5/100))

  #This is the estimated number of severe positive cases that will require ventilators.
  impact['impact']['casesForVentilatorsByRequestedTime']=int(impact['impact']['infectionsByRequestedTime']*(2/100))
  impact['severeImpact']['casesForVentilatorsByRequestedTime']=int(impact['severeImpact']['infectionsByRequestedTime']*(2/100))
   
  #dollars in flight estimate
  avgDailyIncomeInUSD=data['region']["avgDailyIncomeInUSD"]
  avgDailyIncomePopulation=data['region']["avgDailyIncomePopulation"]
  timeindays=int(timenormaliseday(data['periodType'],data['timeToElapse']))

  impact['impact']['dollarsInFlight']=int(impact['impact']['infectionsByRequestedTime']*(avgDailyIncomeInUSD*avgDailyIncomePopulation*timeindays))
  impact['severeImpact']['dollarsInFlight']=int(impact['severeImpact']['infectionsByRequestedTime']*(avgDailyIncomeInUSD*avgDailyIncomePopulation*timeindays))


  impact["estimate"] = {'impact':impact['impact'], 'severeImpact':impact['severeImpact']} 
  del impact["impact"]
  del impact["severeImpact"]
#   app_json = json.dumps(impact)
  return impact
# testone=estimator(data_jsonx)
# print(testone)