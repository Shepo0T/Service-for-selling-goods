# Используем официальный образ Python 3.12.3
FROM python:3.12.3-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем необходимые зависимости для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем команду для запуска приложения
CMD ["fastapi", "run" "src/main.py", "--host", "0.0.0.0", "--port", "8000"]