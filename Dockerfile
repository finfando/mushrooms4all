FROM python:3.6-slim
USER root

RUN apt-get -y update
RUN pip install flask sklearn pandas numpy

COPY . /application
WORKDIR /application

CMD flask run --host=0.0.0.0