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
from logging.config import dictConfig
import logging
from .config import LogConfig

# model dependencies imports
import pandas as pd
import numpy as np
import time

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

security = HTTPBasic()

# set up logger
dictConfig(LogConfig().dict())
logger = logging.getLogger("latam-ml-service")


def model_deserializer(model):
    try:
        return pickle.load(model)
    except Exception as e:
        logger.error(f"Invalid Model: {e}")
        raise


class Flight(BaseModel):
    Vlo_l: str
    Ori_l: str
    Des_l: str
    Emp_l: str

    def _flight_to_df(self):
        return pd.read_csv(
            "/docs/SRE-challenge/datasets/x_test.csv",
            nrows=1,
            skiprows=int(self.Vlo_l),
            header=None,
        ).to_numpy()

    def predict(self):
        model_version = os.getenv("model_version")
        with open(f"../Latam_flight_model.{model_version}.pkl", "rb") as modelfile:
            model = model_deserializer(modelfile)
            try:
                return {
                    "Prediction": "Low delayed probability"
                    if int(model.predict(self._flight_to_df())) > 0
                    else "High delayed probability"
                }
            except Exception as e:
                logger.error(f"Invalid Prediction {e}")
                return {"error": str(e)}


app = FastAPI(
    title="LatamMLAPI",
    version="0.0.1",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)


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
