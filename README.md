# Описание проекта
YaMDb - проект, собирающий отзывы на произведения(книги, фильмы, музыка и т.д.). 
Сами произведения в проекте не хранятся.
### Технологии
- [Django REST Framework] - is a powerful and flexible toolkit for building Web APIs.
- [Simple JWT] - a JSON Web Token authentication plugin for the Django REST Framework.
### Команды для запуска приложения в режиме разработки
- перейти в директорию с проектом

```cd /<путь-до-директории>/```
- создать виртуальное окружение, активировать

```python3 -m venv venv```

```. venv/bin/activate```
- установить зависимости

```python -m pip install -r requirements.txt```
- применить миграции для создания таблиц БД

```python manage.py migrate```
- запустить приложение

```python manage.py runserver```
