# Використовуємо офіційний базовий образ Python
FROM python:3.11-slim

# Встановлюємо необхідні залежності
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копіюємо код додатка в контейнер
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Задаємо точку входу в програму
CMD ["python", "main.py"]
