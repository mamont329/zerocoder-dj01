from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import BootstrapAuthForm

app_name = 'dj05_2'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='dj05_2/login.html',
        authentication_form=BootstrapAuthForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dj05_2:index'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
