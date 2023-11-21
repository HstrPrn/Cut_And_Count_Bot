from datetime import datetime as dt

from api import app, db


class BaseModel:
    """
    Базовая модель, описывающая дополнительные методы.
    """
    def to_dict(self):
        return {
            'id': self.id,
            'original_url': self.original_url,
            'short_path': self.short_path,
            'counter': self.counter,
            'created': self.created
        }

    def save(self):
        db.session.add(self)
        db.session.commit()


class Url(BaseModel, db.Model):
    """ Модель Url"""

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String, nullable=False, unique=True)
    short_path = db.Column(db.String(8), nullable=False, unique=True)
    counter = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime(), default=dt.utcnow)

    def __str__(self):
        return f'Url {self.original_url}'

    def __repr__(self):
        return f'Url {self.original_url}'


with app.app_context():
    db.create_all()
