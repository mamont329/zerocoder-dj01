from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'dj05_1/index.html'


class ProfileView(TemplateView):
    template_name = 'dj05_1/profile.html'
