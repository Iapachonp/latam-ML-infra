
ARG version=3.9.16-slim
FROM python:${version}
RUN mkdir -p /app/src
COPY ./requirements.txt /app
COPY ./model-requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  
RUN pip install --no-cache-dir --upgrade -r /app/model-requirements.txt  
COPY ./src/ /app/src/
COPY ./entry-point.sh .
COPY ./version.txt .
ARG arg_model_version
ENV model_version $arg_model_version
ENTRYPOINT ["/entry-point.sh"]
