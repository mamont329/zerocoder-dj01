from django.shortcuts import render

# Список уроков. Чтобы добавить новый урок — допиши одну строку сюда.
LESSONS = [
    {
        'title': 'Урок DJ01',
        'desc': 'Маршрутизация и вьюхи: страницы data и test на голом HttpResponse.',
        'url': '/dj01/',
    },
    {
        'title': 'Урок DJ02',
        'desc': 'Шаблоны и Bootstrap: 4 страницы на общем каркасе base.html.',
        'url': '/dj02/',
    },
]


def index(request):
    context = {'lessons': LESSONS}
    return render(request, 'home/index.html', context)
