FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Almaty
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "cd store && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]