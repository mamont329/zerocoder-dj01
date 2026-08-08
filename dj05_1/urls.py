from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import BootstrapAuthForm

app_name = 'dj05_1'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # Встроенные вьюхи-классы Django для входа и выхода:
    path('login/', auth_views.LoginView.as_view(
        template_name='dj05_1/login.html',
        authentication_form=BootstrapAuthForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dj05_1:index'), name='logout'),
]
