
ARG version=3.9.16-slim
FROM python:${version}
RUN mkdir -p /app/src
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt  
COPY ./src/ /app/src/
COPY ./entry-point.sh .
COPY ./version.txt .
CMD '/entry-point.sh'
