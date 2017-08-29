FROM python:3.6.2

WORKDIR /app
ADD requirements.txt /app
RUN pip install --no-cache-dir -q -r requirements.txt

ADD ./project /app/project
WORKDIR /app/project

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

CMD gunicorn project.wsgi -b 0.0.0.0:$PORT