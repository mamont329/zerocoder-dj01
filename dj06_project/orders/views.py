from django.http import HttpResponse

from .models import Order


def order_list(request):
    orders = Order.objects.select_related('user').all()
    rows = ''.join(
        f'<li>{o.product} — {o.price} ₽ — {o.user.username}</li>' for o in orders
    )
    return HttpResponse(f'<h1>Заказы</h1><ul>{rows or "<li>пусто</li>"}</ul>')
