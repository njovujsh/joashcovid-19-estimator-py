from pydantic import BaseModel,ValidationError, validator

class Region(BaseModel):
    name: str
    avgAge: float
    avgDailyIncomeInUSD: float
    avgDailyIncomePopulation: float

    # https://pydantic-docs.helpmanual.io/usage/validators/
    #Validate error handling 
    # @validator('name')
    # def name_must_contain_(self,cls, v):
    #     if ' ' not in v:
    #         raise ValueError('must contain a space')
    #     return v.title()

class IntialData(BaseModel):
    region:Region
    periodType: str
    timeToElapse:int
    reportedCases:int
    population:int
    totalHospitalBeds:int