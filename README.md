# API Backend для сервиса покупок

## Описание

Этот проект представляет собой backend API для сервиса покупок, который позволяет пользователям регистрироваться, аутентифицироваться и управлять своей корзиной покупок. API построен с использованием FastAPI, PostgreSQL и SQLAlchemy.

## Установка

1. **Клонируйте репозиторий**:
   ```sh
   git clone https://github.com/your_username/your_repo.git
   cd your_repo

2. Создайте файл .env:
Создайте файл .env в корневой директории проекта с следующим содержимым:
    ```sh
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=db
    POSTGRES_PORT=
    POSTGRES_DB=
    ADMIN_PASSWORD=
    #JWT Settings
    JWT_ALG=HS256
    JWT_EXP=210
    JWT_SECRET=SECRET

3. Соберите и запустите Docker-контейнеры:   
    ```sh
   docker-compose up --build

4. API будет доступен по адресу `http://localhost:8000`.

## Использование
 # Эндпоинты
    Регистрация пользователя: POST /api/v1/users/register
    Аутентификация пользователя: POST /api/v1/auth/login
    Создание продукта: POST /api/v1/products/create (только для администратора)
    Обновление продукта: PUT /api/v1/products/update/{product_id} (только для администратора)
    Удаление продукта: DELETE /api/v1/products/delete/{product_id} (только для администратора)
    Добавление в корзину: POST /api/v1/cart/add_product
    Удаление из корзины: DELETE /api/v1/cart/remove_product/{product_id}
    Очистка корзины: DELETE /api/v1/cart/clear_cart
    