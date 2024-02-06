# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn


RUN apt-get update && apt-get install -y nginx

RUN python manage.py collectstatic --noinput
EXPOSE 8000
EXPOSE 80

CMD service nginx start && gunicorn crud_project.wsgi:application -b 0.0.0.0:8000
