FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY /devchallenge /app/
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
VOLUME /app