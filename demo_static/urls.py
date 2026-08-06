from django.urls import path

from . import views

app_name = 'demo_static'

urlpatterns = [
    path('', views.index, name='index'),
]
