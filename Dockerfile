FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ARG SECRET_KEY=default_secret_key
ARG DEBUG=True
ARG ALLOWED_HOSTS=*

EXPOSE 8000

# RUN ["python", "manage.py", "runserver", "0.0.0.0:8000"]
