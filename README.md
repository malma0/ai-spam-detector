AI Spam Detector

Система для определения спам-сообщений с использованием искусственного интеллекта.

Проект разработан на Python с использованием FastAPI, PostgreSQL и модели машинного обучения для классификации текста на SPAM / NOT SPAM.

Используемые технологии
Backend
Python 3.11+
FastAPI
SQLAlchemy
Pydantic
Uvicorn
База данных
PostgreSQL
Docker / Docker Compose
AI / Machine Learning
Scikit-learn
TF-IDF Vectorizer
Logistic Regression
Frontend
HTML5
CSS3
JavaScript
Возможности проекта
Анализ текста на спам
Определение вероятности спама
История запросов
REST API
Swagger документация
Проверка состояния системы
Работа с PostgreSQL
Docker контейнер для базы данных
Структура проекта
ai-spam-detector/
│
├── backend/
│   ├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── main.py
│   ├── requirements.txt
│   └── docker-compose.yml
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
└── README.md
Установка проекта
1. Клонирование проекта
git clone <repository_url>
cd ai-spam-detector
Настройка Backend
2. Переход в backend
cd backend
3. Создание виртуального окружения
python -m venv venv
4. Активация окружения
Linux / Ubuntu
source venv/bin/activate
Windows
venv\Scripts\activate
5. Установка зависимостей
pip install -r requirements.txt
Запуск PostgreSQL через Docker
6. Запуск контейнера
docker compose up -d
Проверка контейнера
docker ps

Если контейнер работает, будет отображён PostgreSQL на порту 5432.

Запуск Backend
7. Запуск FastAPI сервера
python -m uvicorn app.main:app --reload

Backend будет доступен по адресу:

http://127.0.0.1:8000
Swagger документация

После запуска backend доступна Swagger документация:

http://127.0.0.1:8000/docs

Через Swagger можно:

тестировать API
отправлять POST запросы
просматривать ответы сервера
Запуск Frontend
8. Открытие frontend

Открыть файл:

frontend/index.html

или использовать Live Server в VS Code.

Frontend обычно работает по адресу:

http://127.0.0.1:5500
Основные API endpoints
Проверка состояния системы
GET /health
Анализ текста
POST /analyze

Пример запроса:

{
  "text": "Вы выиграли айфон, перейдите по ссылке"
}
Получение истории запросов
GET /history
Пример работы системы
SPAM
Вы выиграли айфон, перейдите по ссылке и заберите приз

Результат:

SPAM
NOT SPAM
Привет, как дела?

Результат:

NOT SPAM
Docker

Для проекта используется Docker контейнер PostgreSQL.

Проверка контейнеров:

docker ps

Остановка контейнеров:

docker compose down