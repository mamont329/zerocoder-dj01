from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import CustomUserCreationForm


class IndexView(TemplateView):
    template_name = 'index.html'


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')   # после регистрации — на вход


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'        # login_url берётся из settings.LOGIN_URL
