from django.shortcuts import render, redirect

from .forms import FilmForm
from .models import Film


def film_list(request):
    # Все фильмы из БД для страницы вывода.
    films = Film.objects.all()
    return render(request, 'dj04/film_list.html', {'films': films})


def film_add(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)   # форма с данными пользователя
        if form.is_valid():             # прошла проверку?
            form.save()                 # сохранили фильм в БД
            return redirect('dj04:film_list')   # ушли на страницу вывода
        else:
            error = 'Форма заполнена неверно'
    else:
        form = FilmForm()               # первый заход — пустая форма
    return render(request, 'dj04/film_add.html', {'form': form, 'error': error})
