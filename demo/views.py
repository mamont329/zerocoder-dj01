from django.shortcuts import render

# Список демо-объяснений раздела «Демо».
# Новая демка = дописать одну строку сюда (title/desc/url).
DEMOS = [
    {
        'title': 'demo_for — тег {% for %}',
        'desc': 'Перебор списка в шаблоне: forloop.counter/first/last и {% empty %}.',
        'url': '/demo/for/',
    },
    {
        'title': 'demo_static — свои static-файлы',
        'desc': 'Свой CSS и картинка через {% load static %} и {% static %} (не CDN).',
        'url': '/demo/static/',
    },
]


def index(request):
    return render(request, 'demo/index.html', {'demos': DEMOS})
