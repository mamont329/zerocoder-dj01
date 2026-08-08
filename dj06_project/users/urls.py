from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='list'),
    path('orders-count/', views.orders_count, name='orders_count'),
]
