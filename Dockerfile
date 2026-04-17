FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run collectstatic at build time (Whitenoise serves these)
RUN python manage.py collectstatic --noinput

# Use $PORT so Cloud Run can inject its port
# Temporarily comment out migrate to test if container starts
CMD ["sh", "-c", "gunicorn joblink.wsgi:application --bind 0.0.0.0:$PORT --timeout 60"]