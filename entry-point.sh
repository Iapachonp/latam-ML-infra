#!/bin/sh

getModel(){
  set -e
  model_version=`cat version.txt`
  if [ "$env" == "local" ] ; then 
    cp "/Model/Latam_flight_model.${model_version}.pkl" ./app/
  else
    cp "/Latam_flight_model.${model_version}.pkl" ./app/
  fi
}

# MAIN code 

# Sets and gets the model version to serve 
getModel
export model_version=`cat version.txt`
echo "${model_version}"
# Start service at port 8000
cd app/src/
gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 main:app
# uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8070
