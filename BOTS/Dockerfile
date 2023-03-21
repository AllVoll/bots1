# Базовый образ
FROM python:3.11-slim as base

# Установка зависимостей
RUN apt-get update && apt-get install -y gcc

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    libgomp1

# Установка ta-lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz \
    && tar -xzf ta-lib-0.4.0-src.tar.gz \
    && cd ta-lib/ \
    && ./configure --prefix=/usr \
    && make \
    && make install \
    && cd .. \
    && rm -rf ta-lib/ ta-lib-0.4.0-src.tar.gz

# Инициализация проекта
WORKDIR /app

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копирование файла с зависимостями
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода в контейнер
COPY . /app

# Установка переменных окружения для Flask
ENV FLASK_APP=myflaskapp.py
ENV FLASK_ENV=development

# Запуск приложения Flask при запуске контейнера
CMD flask run --host=0.0.0.0



