FROM python:3.6.2

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD ./project /app/project
WORKDIR /app/project

EXPOSE 8000

CMD gunicorn project.wsgi -b 0.0.0.0:8000