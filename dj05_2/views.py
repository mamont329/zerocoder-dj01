from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import BootstrapUserCreationForm


class IndexView(TemplateView):
    template_name = 'dj05_2/index.html'


class RegisterView(CreateView):
    form_class = BootstrapUserCreationForm
    template_name = 'dj05_2/register.html'
    # После успешной регистрации — на страницу входа (как требует задание).
    success_url = reverse_lazy('dj05_2:login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dj05_2/profile.html'
    # Гостя, который сюда полез, кинет на login (и вернёт назад после входа).
    login_url = reverse_lazy('dj05_2:login')
