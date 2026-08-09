from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user/<int:telegram_id>/', views.user_info, name='user_info'),
]
