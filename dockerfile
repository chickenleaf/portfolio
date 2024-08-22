FROM python:3.10-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /django_portfolio

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

CMD gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000