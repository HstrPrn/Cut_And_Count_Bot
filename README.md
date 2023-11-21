# Cut And Count Bot

Cut And Count Bot - телеграм бот для укорачивания длинных ссылок.

# Stack

- [Python 3.9.18](https://www.python.org/downloads/release/python-3918/)
- [Flask 3.0.0](https://flask.palletsprojects.com/en/3.0.x/changes/)
- [Flask-SQLAlchemy 3.1.1](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [PyTelegramBotApi 4.14.0](https://pypi.org/project/pyTelegramBotAPI/)

# Локальное развертываение

Клонируйте проект на свой компьютер

    git clone https://github.com/HstrPrn/foodgram-project-react

В корневой папке создайте файл с переменными окружения

    touch .env

Шаблон переменных окружения

    API_URL=http://localhost:5000/
    DEBUG=True
    FLASK_APP=api
    SECRET_KEY=<secret_key>
    SQLALCHEMY_DATABASE_URI=sqlite:///db.db

    BOT_TOKEN=<telegram_bot_token>

Настройте и запустите виртуальное окружение

    python3 -m venv venv
    source venv/bin/activate

Находясь в корневой папке обновите пакетный менеджер и установите зависимости

    pip install --upgrade pip
    pip install -r Bot/requirements.txt -r Web/requirements.txt

Запустите приложения

    python3 Web/run.py 
    python3 Bot/main.py

# Авторы

[Иван Ефремов](https://github.com/HstrPrn)
