"""Telegram-бот (telebot) — КЛИЕНТ Django API.

Запускать отдельным процессом: python telegram_bot.py
Django-API при этом должен быть поднят (по умолчанию http://127.0.0.1:8003).
"""
import os
from pathlib import Path

import requests
import telebot
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# Адрес нашего Django API (не секрет — можно переопределить в .env)
API_URL = os.getenv('API_URL', 'http://127.0.0.1:8003/api')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # Данные пользователя берём из самого сообщения Telegram
    tg_user = message.from_user
    data = {
        'telegram_id': tg_user.id,
        'username': tg_user.username or tg_user.first_name or '',
    }

    # Шлём их в Django API (POST /api/register/) — бот тут обычный HTTP-клиент
    try:
        resp = requests.post(f'{API_URL}/register/', json=data, timeout=5)
    except requests.RequestException:
        bot.reply_to(message, '⚠️ Сервер недоступен, попробуйте позже.')
        return

    if resp.status_code == 201:
        bot.reply_to(message, f'✅ {data["username"]}, вы успешно зарегистрированы!')
    elif resp.status_code == 200:
        bot.reply_to(message, f'ℹ️ {data["username"]}, вы уже были зарегистрированы.')
    else:
        bot.reply_to(message, f'❌ Ошибка регистрации (код {resp.status_code}).')


if __name__ == '__main__':
    print('Бот запущен, ждёт сообщений...')
    bot.infinity_polling()
