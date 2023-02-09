ARG version=3.9.16-slim
FROM python:${version}

RUN mkdir /lib-test  
COPY ./test-requirements.txt /lib
COPY ./requirements.txt /lib

RUN pip install --no-cache-dir --upgrade -r /lib/requirements.txt  
RUN pip install --no-cache-dir --upgrade -r /lib/test-requirements.txt  





