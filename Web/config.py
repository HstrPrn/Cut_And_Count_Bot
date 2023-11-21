import os

import dotenv


dotenv.load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///devdb.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
