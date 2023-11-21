from http import HTTPStatus

from api import app
from flask import redirect, request

from . import const
from .models import Url
from .utils import create_new_link, get_or_create, is_correct_url


@app.post('/')
def create_short_orl():
    original_url: str = request.get_json().get('url')
    if not is_correct_url(original_url):
        return (
            {'error': 'invalid value'},
            HTTPStatus.BAD_REQUEST
        )
    obj, created = get_or_create(Url, original_url=original_url)
    if not created:
        return {'url': obj.short_path}, HTTPStatus.OK
    short_url: str = create_new_link()
    obj.short_path: str = short_url
    obj.save()
    return {'url': obj.short_path}, HTTPStatus.CREATED


@app.get('/')
def get_all_urls():
    return {'urls': [obj.to_dict() for obj in Url.query.all()]}, HTTPStatus.OK


@app.get('/<path:short_path>/')
def redirect_to_original_url(short_path: str):
    if len(short_path) != const.PATH_LENGH:
        return redirect(const.DEFAULT_REDIRECT_URL)
    obj: Url = Url.query.filter_by(short_path=short_path).first()
    if not obj:
        return redirect(const.DEFAULT_REDIRECT_URL)
    obj.counter += 1
    obj.save()
    response = redirect(obj.original_url)
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response
