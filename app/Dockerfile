# syntax=docker/dockerfile:1

FROM python:alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

CMD gunicorn --bind 0.0.0.0:8010 wsgi:app