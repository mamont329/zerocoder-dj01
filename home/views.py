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
    {
        'title': 'Урок DJ03',
        'desc': 'Модели и БД: новости из базы — список и детальная страница.',
        'url': '/dj03/',
    },
    {
        'title': 'Урок DJ04',
        'desc': 'Формы: добавление фильма через форму на странице и вывод из БД.',
        'url': '/dj04/',
    },
    {
        'title': 'Урок DJ05 · задание 1',
        'desc': 'Аутентификация: маршруты и страницы (index, profile, login, logout), навигация.',
        'url': '/dj05_1/',
    },
    {
        'title': 'Урок DJ05 · задание 2',
        'desc': 'Регистрация (UserCreationForm) + профиль только для авторизованных (LoginRequiredMixin).',
        'url': '/dj05_2/',
    },
]


def index(request):
    context = {'lessons': LESSONS}
    return render(request, 'home/index.html', context)
