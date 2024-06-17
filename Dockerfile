FROM python:3.10

COPY requirements.txt /temp/requirements.txt
COPY web-app /web-app

WORKDIR /web-app
EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password app-user


USER app-user
