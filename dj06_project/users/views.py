from django.contrib.auth import get_user_model
from django.http import HttpResponse


def user_list(request):
    # get_user_model() вернёт АКТИВНУЮ модель пользователя (users.CustomUser),
    # без жёсткой привязки к конкретной модели.
    User = get_user_model()
    users = User.objects.all()
    rows = ''.join(f'<li>{u.username} — тел.: {u.phone_number or "—"}</li>' for u in users)
    return HttpResponse(f'<h1>Пользователи</h1><ul>{rows or "<li>пусто</li>"}</ul>')


def orders_count(request):
    # Ленивый импорт: модель ДРУГОГО приложения импортируем ВНУТРИ функции,
    # а не вверху файла — так не создаём зависимость на уровне модуля (защита от циклов).
    from orders.models import Order
    return HttpResponse(f'<h1>Всего заказов в системе: {Order.objects.count()}</h1>')
