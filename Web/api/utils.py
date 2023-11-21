import random
import string
from typing import Tuple
from urllib.parse import urlparse

from . import const
from .models import Url


def create_new_link(length: int = const.PATH_LENGH) -> str:
    """Создание случайного строкового значения для пути урла."""
    chars: str = string.ascii_lowercase + string.digits
    return ''.join([random.choice(chars) for _ in range(length)])


def get_or_create(obj: Url, **kwargs) -> Tuple[Url, bool]:
    """
    Получение из базы или создание нового объекта модели Url.
    """
    res = obj.query.filter_by(**kwargs).first()
    if not res:
        return obj(**kwargs), True
    return res, False


def is_correct_url(url: str) -> bool:
    """
    Проверка ссылки на наличие правильного протокола и netloc'a.
    """
    result = urlparse(url)
    return all((result.scheme in ('http', 'https'),  result.netloc))
