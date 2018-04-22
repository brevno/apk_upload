FROM python:3


RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app
COPY docker/web/settings.py /app/file_upload/

