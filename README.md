# Учебный проект API для Yatube

Написан API для проекта Yatube. Изучал возможности API.
Используются фреймворки Django и DRF.
Формат передачи данных - JSON.
У неаутентифицированных пользователей доступ к API только на чтение.
Используются версия Python 3.7

## Как запустить проект:

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры API запросов:

### Эндпоинты для взаимодействия http://127.0.0.1:8000/api/v1/... :

  .../api-token-auth/ (POST): передаём логин и пароль, получаем токен.
  
  .../posts/ (GET, POST): получаем список всех постов или создаём новый пост.
  Пример:
  POST Request:
  ```
  {
      "text": "text"
  }
  ```
  
  Response:
  
  ```
  {
    "id": 14,
    "text": "Веtext",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
  }
  ```
  
  .../posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
  
  .../groups/ (GET): получаем список всех групп.
  
  .../groups/{group_id}/ (GET): получаем информацию о группе по id.
  
  .../posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
  Пример:
  POST Request:
  ```
  {
      "text": "text"
  }
  ```
  
  Response:
  
  ```
  {
    "id": 4,
    "author": "anton",
    "post": 14,
    "text": "text",
    "created": "2021-06-01T10:14:51.388932Z"
  }
  ```
  
  .../posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)

