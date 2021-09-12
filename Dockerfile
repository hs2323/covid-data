FROM python:3.9.7

RUN mkdir /data
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

VOLUME ["/data"]

CMD python -m covid --path /data
