# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# FROM ubuntu:20.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update

RUN apt-get install -y python3-tk

COPY . .

# CMD [ "python", "-m", "bacilo_de_Koch.scripts.scripts_all" ]
