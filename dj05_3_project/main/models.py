from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # email делаем обязательным и уникальным
    email = models.EmailField('Электронная почта', unique=True)
    # телефон — необязательное поле
    phone_number = models.CharField('Номер телефона', max_length=20, blank=True)

    def __str__(self):
        return self.username
