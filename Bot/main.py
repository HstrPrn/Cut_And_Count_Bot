import os
from typing import List
from urllib.parse import urlparse

import telebot
import dotenv
import requests


dotenv.load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
API_URL = os.getenv('API_URL', 'http://127.0.0.1:5000/')


bot = telebot.TeleBot(TOKEN)


def get_urls_list() -> list[dict]:
    """Получение списка урлов."""
    return requests.get(API_URL).json().get('urls')


def get_short_url(original_url: str) -> str:
    """Получение нового урла."""
    data: dict = {'url': original_url}
    return requests.post(API_URL, json=data).json().get('url')


def is_correct_url(url: str) -> bool:
    """Проверка урла наличие кореектного протокола и netlog'а. """
    res = urlparse(url)
    return all((res.scheme in ('http', 'https'), res.netloc))


@bot.message_handler(commands=['start'])
def start(message):
    reply_message = (
        f'Для полученя сокращенной ссылки просто напишите ссылку, '
        f'которую нужно сократить. ссылка должна начинаться с "http(s)://".\n'
        f'Пример: https://google.com\n\n'
        f'Чтобы получить список всех ссылок, введите команду "/list".')
    bot.send_message(message.chat.id, reply_message)


@bot.message_handler(commands=['list'])
def send_all_urls(message):
    urls_list: List[dict, None] = get_urls_list()
    if not urls_list:
        bot.send_message(message.chat.id, 'Empty list')
    else:
        reply_message: str = ''
        for url in urls_list:
            reply_message += '{url}  {counter}\n'.format(
                url=API_URL + url.get('short_path'),
                counter=str(url.get('counter'))
            )
        bot.send_message(
            message.chat.id,
            text=reply_message,
            disable_web_page_preview=True
        )


@bot.message_handler(func=lambda message: True)
def send_short_url(message):
    url: str = message.text
    if not is_correct_url(url):
        bot.send_message(message.chat.id, 'Неправильная ссылка')
    else:
        short_url = get_short_url(url)
        bot.send_message(
            message.chat.id,
            API_URL + short_url,
            disable_web_page_preview=True
        )


if __name__ == '__main__':
    bot.infinity_polling()
