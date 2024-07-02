FROM python:3.12-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations \
    && python manage.py migrate

EXPOSE 8000

VOLUME ["/app/db.sqlite3"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]