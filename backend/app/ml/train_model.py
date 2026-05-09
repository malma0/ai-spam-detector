import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


training_texts = [
    "Поздравляем вы выиграли приз",
    "Получите бесплатные деньги прямо сейчас",
    "Срочно перейдите по ссылке и получите подарок",
    "Вы выиграли айфон нажмите сюда",
    "Купите дешевые товары со скидкой 90 процентов",
    "Ваш аккаунт заблокирован перейдите по ссылке",
    "Заработайте деньги без вложений",
    "Бесплатный бонус только сегодня",
    "Вы получили денежный перевод подтвердите данные",
    "Супер акция только сейчас",

    "Привет как дела",
    "Ты сегодня дома",
    "Давай встретимся вечером",
    "Я отправил тебе файл",
    "Во сколько начнется пара",
    "Можешь позвонить позже",
    "Спасибо за помощь",
    "Завтра нужно сдать работу",
    "Я буду через 10 минут",
    "Проверь пожалуйста сообщение",
]

training_labels = [
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",
    "SPAM",

    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
    "NOT_SPAM",
]


model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True)),
    ("classifier", LogisticRegression())
])


model.fit(training_texts, training_labels)

joblib.dump(model, "app/ml/spam_model.pkl")

print("Модель обучена и сохранена в app/ml/spam_model.pkl")