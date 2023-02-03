ARG version=3.9.16-slim
FROM python:${version}

# Model source code and dependencies build
RUN mkdir -p /app/src
COPY ./src/ /app/src/
COPY ./requirements.txt /app
COPY ./model-requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  
RUN pip install --no-cache-dir --upgrade -r /app/model-requirements.txt  

# Target model version to build 
ARG arg_model_version
ENV model_version $arg_model_version

# Copy Micro-service scripts and needed docs
COPY ./entry-point.sh .
COPY ./version.txt .
COPY ./Latam_flight_model.$arg_model_version.pkl . 

# micro service entry point 
ENTRYPOINT ["/entry-point.sh"]
