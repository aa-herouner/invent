# FROM python:3.12

# RUN apt-get update && apt-get install -y nano


# ENV  PYTHONDONTWRITEBYTECODE=1
# ENV  PYTHONUNBUFFERED=1

# WORKDIR /app

# COPY ./requirements.txt /app

# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . /app

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0 : 8000"]
# Use official Python image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y nano

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Copy static and migration files

RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput
# RUN python manage.py createsuperuser --noinput --username admin --email

# Expose the port your Django app runs on
EXPOSE 8000

# Default command
#  CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "inventory.wsgi:application", "--bind", "0.0.0.0:$PORT"]

