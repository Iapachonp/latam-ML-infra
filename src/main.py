from typing import Optional
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
from conf.config import LogConfig
from conf.config import DataBaseConfig

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

# set up data base
db = DataBaseConfig()


def model_deserializer(model):
    try:
        return pickle.load(model)
    except Exception as e:
        logger.error(f"Invalid Model: {e}")
        raise


class Flight(BaseModel):
    Vlo_l: str
    Fecha_l: Optional[str] = ""
    O_vlo: Optional[str] = ""
    O_fecha: Optional[str] = ""
    flight_type: Optional[str] = ""
    airline: Optional[str] = ""

    def _get_flight_from_db(self):
        return pd.read_csv(
            db.path,
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
                    if int(model.predict(self._get_flight_from_db())) > 0
                    else "High delayed probability"
                }
            except Exception as e:
                logger.error(f"Invalid Prediction {e}")
                return {"error": str(e)}

    def exists(self):
        try:
            assert (
                pd.read_csv(
                    db.path,
                    nrows=1,
                    skiprows=int(self.Vlo_l),
                    header=None,
                )
                .to_numpy()
                .any()
            )
            return True
        except Exception as e:
            logger.error(f"Invalid Flight {e}")
            return False


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


@app.get("/check-flight")
async def check_flight(Vlo_l: str):
    dummy_flight = Flight(Vlo_l=Vlo_l)
    return (
        {f"Flight {Vlo_l} exists"}
        if dummy_flight.exists()
        else {f"Flight {Vlo_l} doesn't exists"}
    )


@app.post("/predict-flight")
async def predict_flight(flight: Flight):
    return flight.predict() if flight.exists() else {f"Flight {flight.Vlo_l} doesn't exists"}
