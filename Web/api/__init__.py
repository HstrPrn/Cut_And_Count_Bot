import config

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import dotenv


app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


dotenv.load_dotenv()

from . import models, utils, views, const
