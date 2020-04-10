import json
import sys
from helpers import timenormaliseday


data_json =  '{"region":{"name":"Africa","avgAge":19.7,"avgDailyIncomeInUSD":5,"avgDailyIncomePopulation":0.71}, "periodType":"days","timeToElapse":58,"reportedCases":674,"population":66622705,"totalHospitalBeds":1380614}'



def estimator(data_input):
  data= json.loads(data_input)
  reportedCases=int(data["reportedCases"])
  impact= {
  'data':data, #the input data you got
  'impact':{'currentlyInfected':reportedCases*10}, #your best case estimation,
  'severeImpact':{'currentlyInfected':reportedCases*50} #your severe case estimationl,
  }
  factor=int(timenormaliseday(data['periodType'],data['timeToElapse'])*1/3)
  # Edited output by number of days per infected people
  impact['impact']['infectionsByRequestedTime']=impact['impact']['currentlyInfected']*2^factor
  impact['severeImpact']['infectionsByRequestedTime']=impact['severeImpact']['currentlyInfected']*2^factor
#   impact['infectionsByRequestedTime']={
#     'impact':impact['impact']['currentlyInfected']*2^factor,
#     'severeImpact':impact['severeImpact']['currentlyInfected']*2^factor
#   }   
  app_json = json.dumps(impact)
  print(app_json)
  return impact


estimator(data_json)