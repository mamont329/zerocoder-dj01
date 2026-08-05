from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Главная страница DJ01<br>'
        '<a href="/data/">Открыть data</a><br>'
        '<a href="/test/">Открыть test</a>'
    )


def data(request):
    return HttpResponse('Это страница DATA')


def test(request):
    return HttpResponse('А это страница TEST')
