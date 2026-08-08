from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # email уже есть в разделе Personal info; добавляем телефон
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('phone_number',)}),
    )
