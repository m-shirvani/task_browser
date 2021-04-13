# pull official base image
FROM python:3.9.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry export --without-hashes --dev -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py collectstatic --no-input
