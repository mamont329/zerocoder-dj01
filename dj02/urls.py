from django.urls import path

from . import views

app_name = 'dj02'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]
