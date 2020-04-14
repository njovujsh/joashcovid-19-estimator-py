import time
from fastapi import FastAPI,Response,Request
from fastapi.responses import RedirectResponse,StreamingResponse
from fastapi.encoders import jsonable_encoder

from src.estimator import estimator
from src.models import IntialData
from src.helpers import read_config
#from dict to xml
from dicttoxml import dicttoxml
#login
import logging
# logging.basicConfig(level=logging.INFO, file='src/app.log')
app = FastAPI()

@app.get("/")
async def read_root():
    return RedirectResponse("http://127.0.0.1:8000/redoc")


@app.post("/api/v1/on-covid-19/")
@app.post("/api/v1/on-covid-19/json")
async def covidestimator(data:IntialData):
    app_json=data.json()
    return estimator(app_json)

@app.post("/api/v1/on-covid-19/xml")
#https://fastapi.tiangolo.com/advanced/custom-response/
async def covidestimatorxml(data:IntialData):
    app_json=data.json()
    starndard= estimator(app_json)
    xml = dicttoxml(starndard)
    return Response(content=xml, media_type="application/xml")

@app.get("/api/v1/on-covid-19/logs")
async def getlogsrequest():
    file_like = open("src/logs.txt", mode="rb")
    return StreamingResponse(file_like, media_type="text/plain")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    process_time_ms=int(process_time*1000000)
    #start loggin requests and response time
    logging.info("{a}  {b}  {c}  {d} {t}".format(a=request.method, b=request.url.path, c=response.status_code, d=process_time_ms,t="ms"))
    filelog = open("src/logs.txt","a") 
    l="{a}  {b}  {c}  {d}  {t}\n".format(a=request.method, b=request.url.path, c=response.status_code, d=process_time_ms,t="ms")
    filelog.writelines(l)
    filelog.close()
    #end loggin requests and response time
    return response