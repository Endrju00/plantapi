# Python and Linux version
FROM python:3.8.13-alpine

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \
    && apk add -u gcc musl-dev \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . . 

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "plant_api.wsgi:application"]

CMD gunicorn plant_api.wsgi:application --bind 0.0.0.0:$PORT