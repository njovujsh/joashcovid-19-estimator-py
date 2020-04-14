import sys
from src.helpers import timenormaliseday


def estimator(data):
  reportedCases = data["reportedCases"]
  impact= {
  'data':data, #the input data you got
  'impact':{'currentlyInfected':reportedCases*10}, #your best case estimation,
  'severeImpact':{'currentlyInfected':reportedCases*50} #your severe case estimationl,
  }
  factor=int(timenormaliseday(data['periodType'],data['timeToElapse'])*1/3)
  # Edited output by number of days per infected people
  #Challenge 1
  impact['impact']['infectionsByRequestedTime']=impact['impact']['currentlyInfected']*(2**factor)
  impact['severeImpact']['infectionsByRequestedTime']=impact['severeImpact']['currentlyInfected']*(2**factor)
  return impact
