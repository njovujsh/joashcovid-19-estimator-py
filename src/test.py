
# from estimator import sumnumbers
from estimator import estimator
def test_estimator():
    #sample data from sample output
    data_json_sample= '{"region":{"name":"Africa","avgAge":19.7,"avgDailyIncomeInUSD":4,"avgDailyIncomePopulation":0.73}, "periodType":"days","timeToElapse":38,"reportedCases":2747,"population":92931687,"totalHospitalBeds":678874}'
    returnedestimate=estimator(data_json_sample)
    #These estimates are from a sample output input image
    #For Impact
    assert returnedestimate['impact']['currentlyInfected']==27470 #Should be 27470
    assert returnedestimate['impact']['infectionsByRequestedTime']==112517120 #Should be 112517120
    assert returnedestimate['impact']['severeCasesByRequestedTime']==16877568 #Should be 16877568
    assert returnedestimate['impact']['hospitalBedsByRequestedTime']==-16639963 #Should be -16639963
    assert returnedestimate['impact']['casesForICUByRequestedTime']==5625856 #Should be 5625856
    assert returnedestimate['impact']['casesForVentilatorsByRequestedTime']==2250342 #Should be 2250342
    assert returnedestimate['impact']['dollarsInFlight']==12484899635 #Should be 12484899635

    # For Sever Impact
    assert returnedestimate['severeImpact']['currentlyInfected']==137350 #Should be 137350
    assert returnedestimate['severeImpact']['infectionsByRequestedTime']==562585600 #Should be 562585600
    assert returnedestimate['severeImpact']['severeCasesByRequestedTime']==84387840 #Should be 84387840
    assert returnedestimate['severeImpact']['hospitalBedsByRequestedTime']==-84150235 #Should be -84150235
    assert returnedestimate['severeImpact']['casesForICUByRequestedTime']==28129280 #Should be 28129280
    assert returnedestimate['severeImpact']['casesForVentilatorsByRequestedTime']==11251712 #Should be 11251712
    assert returnedestimate['severeImpact']['dollarsInFlight']==62424498176 #Should be 62424498176

if __name__ == "__main__":
    test_estimator()
    print("Everything passed")