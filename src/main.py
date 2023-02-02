from fastapi import Depends, FastAPI, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import types
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from fastapi.exception_handlers import (
    request_validation_exception_handler,
)
import pickle
import os

security = HTTPBasic()


class Flight(BaseModel):
    Vlo_l: str
    Ori_l: str
    Des_l: str
    Emp_l: str

    def predict(self):
        model_version= os.getenv("modelVersion")
        with open( f"../Latam_flight_model:{model_version}.pkl", "rb" ) as modelfile :
            model = pickle.load(modelfile)
            return {"Prediction": model.predict()}


app = FastAPI(
    title="LatamMLAPI",
    version="0.0.1",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)
    # return JSONResponse(
    #   status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #  content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    # )


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}


@app.post("/play-doh")
def play_doh(figure: str):
    return {
        "play-doh figure": figure,
        "build": "yes" if len(figure) > 5 else "no fucking way",
    }


@app.post("/flight")
async def create_flight(flight: Flight):
    return {"This flight departs from": flight.Ori_l, "to": flight.Des_l}


@app.post("/predict-flight")
async def predict_flight(flight: Flight):
    return flight.predict()
