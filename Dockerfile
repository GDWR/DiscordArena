FROM python:3.9-slim-buster

RUN apt-get update
RUN apt-get -y install git

ENV POETRY_VERSION=1.1.6

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /workspace

COPY poetry.lock poetry.toml pyproject.toml /workspace/
RUN poetry install
