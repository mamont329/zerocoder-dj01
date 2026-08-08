from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<h1>mysite</h1>'
        '<p>Учебный проект: архитектура приложений (users + orders).</p>'
        '<ul>'
        '<li><a href="/users/">Пользователи</a></li>'
        '<li><a href="/orders/">Заказы</a></li>'
        '<li><a href="/users/orders-count/">Счётчик заказов (ленивый импорт)</a></li>'
        '<li><a href="/admin/">Админка</a></li>'
        '</ul>'
    )
