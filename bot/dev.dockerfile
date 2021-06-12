FROM python:3.9-slim-buster

RUN apt-get update
RUN pip install flake8 flake8-docstrings

WORKDIR /workspace/bot
COPY requirements.txt .
RUN pip install -r requirements.txt
