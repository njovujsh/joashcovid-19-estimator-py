from fastapi import FastAPI
from src import estimator
from estimator import estimator

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/v1/on-covid-19/{item_id}")
async def covidesimatre(item_id: int, q: str = None):
    #   data_json =  '{"region":{"name":"Africa","avgAge":19.7,"avgDailyIncomeInUSD":4,"avgDailyIncomePopulation":0.73}, "periodType":"days","timeToElapse":38,"reportedCases":2747,"population":92931687,"totalHospitalBeds":678874}'
    return {"item_id": item_id, "q": q}
    # return estimator(data_json)