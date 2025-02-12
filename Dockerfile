FROM python:3.10.12-slim

ENV DOCKER_ENV true

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt requirements.txt

RUN python -m venv venv

ENV PATH="/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /project

CMD ["python" , "app/main.py"]