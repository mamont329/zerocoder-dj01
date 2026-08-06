from django.shortcuts import render


def index(request):
    # 1) Готовим ДАННЫЕ во вьюхе. Это обычный список Python из словарей.
    #    Именно его шаблон будет перебирать тегом {% for %}.
    lessons = [
        {'title': 'Урок DJ01', 'url': '/dj01/', 'topic': 'Маршруты и вьюхи'},
        {'title': 'Урок DJ02', 'url': '/dj02/', 'topic': 'Шаблоны и Bootstrap'},
        {'title': 'Урок DJ03', 'url': '#',      'topic': '(ещё не создан)'},
    ]

    # 2) Пустой список — специально, чтобы показать работу {% empty %}.
    empty_list = []

    # 3) Кладём данные в context — это "мост" из вьюхи в шаблон.
    #    Ключи словаря ('lessons', 'empty_list') станут именами переменных
    #    внутри шаблона.
    context = {
        'lessons': lessons,
        'empty_list': empty_list,
    }

    # 4) render() берёт шаблон, подставляет в него context и возвращает HTML.
    return render(request, 'demo_for/index.html', context)
