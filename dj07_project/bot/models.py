from django.db import models


class TelegramUser(models.Model):
    # ID пользователя в Telegram (большое число, поэтому BigIntegerField), уникальный
    telegram_id = models.BigIntegerField('Telegram ID', unique=True)
    username = models.CharField('Имя пользователя', max_length=150, blank=True)
    created_at = models.DateTimeField('Зарегистрирован', auto_now_add=True)

    def __str__(self):
        return f'{self.username} ({self.telegram_id})'
