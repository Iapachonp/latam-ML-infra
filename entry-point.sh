

function getModel (){
  set -e
  model_version= `cat version.txt` 
  if test[$env == "local"] ; then 
    cp /Model/Latam_flight_model:$model_version.pkl ./src/
  else
    gsutil cp gs://ML-model-bucket/Latam_flight_model:$model_version.pkl ./src/
  fi 
}

# MAIN code 

# Sets and gets the model version to serve 
getModel()
# Start service at port 8000
cd app/src/
uvicorn main:app --host 0.0.0.0 --port $PORT
