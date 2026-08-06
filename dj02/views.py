from django.shortcuts import render


def index(request):
    return render(request, 'dj02/home.html')


def about(request):
    return render(request, 'dj02/about.html')


def services(request):
    return render(request, 'dj02/services.html')


def contacts(request):
    return render(request, 'dj02/contacts.html')
