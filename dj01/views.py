from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Главная страница DJ01<br>'
        '<a href="/dj01/data/">Открыть data</a><br>'
        '<a href="/dj01/test/">Открыть test</a><br><br>'
        '<a href="/">← ко всем урокам</a>'
    )


def data(request):
    return HttpResponse('Это страница DATA')


def test(request):
    return HttpResponse('А это страница TEST')
