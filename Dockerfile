FROM python:3.11.7-slim

RUN mkdir /src
WORKDIR /src
COPY . /src

RUN pip install -r requirements.txt