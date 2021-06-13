FROM python:3.9-slim-buster

RUN apt-get update
RUN pip install poetry

WORKDIR /workspace

ADD pyproject.toml .
RUN poetry install
