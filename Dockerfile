from python:3.9

WORKDIR /apps
RUN pip install pandas
COPY dags .