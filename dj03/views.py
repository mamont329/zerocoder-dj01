from django.shortcuts import render, get_object_or_404

from .models import News_post


def news_list(request):
    # Достаём ВСЕ новости из БД. Свежие — сверху (минус = по убыванию даты).
    news = News_post.objects.all().order_by('-pub_date')
    return render(request, 'dj03/news_list.html', {'news': news})


def news_detail(request, pk):
    # Одна новость по первичному ключу (id). Нет такой — вернём 404.
    post = get_object_or_404(News_post, pk=pk)
    return render(request, 'dj03/news_detail.html', {'post': post})
