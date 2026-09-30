# AI Spam Detector

REST API и веб-интерфейс для определения спама в текстовых сообщениях с помощью ML-моделей. Сервис классифицирует текст как **SPAM / NOT SPAM**, возвращает уверенность модели, хранит историю проверок и умеет кратко пересказывать длинный текст.

## Возможности

- классификация текста на спам с вероятностью (transformer-модель с Hugging Face);
- краткий пересказ текста (`facebook/bart-large-cnn`);
- история запросов в PostgreSQL;
- защита эндпоинтов API-ключом (заголовок `X-API-Key`);
- Swagger-документация и health-check;
- простой веб-интерфейс на HTML/CSS/JS;
- базовая модель TF-IDF + Logistic Regression (`backend/app/ml/train_model.py`) для обучения на своих данных.

## Стек

| Часть | Технологии |
|-------|-----------|
| Backend | Python 3.11+, FastAPI, SQLAlchemy, Pydantic, Uvicorn |
| ML | Hugging Face Transformers, scikit-learn (TF-IDF, Logistic Regression) |
| База данных | PostgreSQL 16 |
| Инфраструктура | Docker, Docker Compose, GitHub Actions |
| Frontend | HTML5, CSS3, JavaScript |

## Структура

```
ai-spam-detector/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI-приложение, CORS, подключение роутеров
│   │   ├── routes/          # analyze, history, health, summarize
│   │   ├── services/        # ml_service: загрузка модели и предсказание
│   │   ├── ml/              # обучение базовой модели и spam_model.pkl
│   │   └── models.py, schemas.py, db.py, config.py, security.py
│   ├── requirements.txt
│   └── DockerFile
├── frontend/                # index.html, styles.css, script.js
├── docker-compose.yml       # backend + PostgreSQL
└── .env.example
```

## Запуск

### Через Docker Compose

```bash
cp .env.example .env
docker compose up -d --build
```

API будет на http://localhost:8000, Swagger на http://localhost:8000/docs.

### Локально

```bash
docker compose up -d postgres    # из корня проекта, только база
cd backend
python -m venv venv
venv\Scripts\activate            # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Frontend

Открыть `frontend/index.html` в браузере или через Live Server в VS Code (http://127.0.0.1:5500).

### Переменные окружения

| Переменная | Назначение |
|-----------|-----------|
| `API_KEY` | ключ для доступа к API (заголовок `X-API-Key`) |
| `DATABASE_URL` | строка подключения к PostgreSQL |
| `MODEL_NAME` | модель классификации с Hugging Face |

## API

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/health` | состояние сервиса |
| POST | `/analyze` | проверка текста на спам |
| POST | `/summarize` | краткий пересказ текста |
| GET | `/history` | история проверок |

Пример запроса:

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -H "X-API-Key: <ваш ключ>" \
  -d '{"text": "Вы выиграли айфон, перейдите по ссылке"}'
```

Пример ответа:

```json
{ "label": "SPAM", "score": 0.9731, "model_name": "mrm8488/bert-tiny-finetuned-sms-spam-detection" }
```
