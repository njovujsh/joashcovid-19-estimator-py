import json
# from estimator import sumnumbers
from estimator import estimator
def test_estimator():
    #sample data from sample output
    data_json_sample= '{"region":{"name":"Africa","avgAge":19.7,"avgDailyIncomeInUSD":4,"avgDailyIncomePopulation":0.73}, "periodType":"days","timeToElapse":38,"reportedCases":2747,"population":92931687,"totalHospitalBeds":678874}'
    returnedestimate=estimator(data=json.loads(data_json_sample))
    print(returnedestimate['estimate']['impact']['currentlyInfected'])
    #These estimates are from a sample output input image
    #For Impact
    

if __name__ == "__main__":
    test_estimator()
    print("Everything passed")