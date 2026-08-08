from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import CustomAuthForm

app_name = 'dj05_3'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='dj05_3/login.html',
        authentication_form=CustomAuthForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dj05_3:index'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
