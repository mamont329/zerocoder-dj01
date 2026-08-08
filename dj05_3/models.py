from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # OneToOne: один профиль ↔ один стандартный User (User НЕ переопределяем)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField('Номер телефона', max_length=20, blank=True)

    def __str__(self):
        return self.user.username
