from django.conf import settings
from django.db import models


class Order(models.Model):
    # Ссылка на пользователя СТРОКОЙ через settings.AUTH_USER_MODEL:
    # приложение orders НЕ импортирует users.models → нет риска циклического импорта.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь',
    )
    product = models.CharField('Товар', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product} ({self.user})'
