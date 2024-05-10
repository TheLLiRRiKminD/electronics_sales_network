# Проект "electronics_sales_network"

Данный проект представляет собой веб-приложение веб-приложение с API-интерфейсом и админ-панелью

## О проекте

Бэкенд обеспечивает API для работы с поставщиками

## Возможности

- Регистрация и авторизация пользователей
- Создание, чтение, обновление и удаление поставщика
- Фильтрацию объектов

## Технологии

- Python
- Django (Django REST framework)
- PostgreSQL (для хранения данных)

## Запуск проекта

1. Установите зависимости:
    - pip install -r requirements.txt

2. Создайте файл `.env` в корневой директории и заполните необходимые переменные окружения:
    - DJANGO_SECRET_KEY=
    - POSTGRES_DB=
    - POSTGRES_USER= 
    - POSTGRES_PASSWORD= 
    - POSTGRES_HOST= 
    - POSTGRES_PORT= 
    - SU_PASSWORD= 
    - SU_EMAIL_ADDRESS=
    - DJANGO_DEBUG= 
    - DJANGO_ALLOWED_HOSTS= 
    - TZ=

3. Примените миграции:
    - python manage.py migrate

4. Создайте суперпользователя базы данных:
    - python manage.py csucustom

5. Запустите сервер:
    - python manage.py runserver

## Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/