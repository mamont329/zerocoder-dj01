from django.urls import path

from . import views

app_name = 'dj04'

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('add/', views.film_add, name='film_add'),
]
