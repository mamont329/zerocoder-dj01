from django.shortcuts import render


def index(request):
    return render(request, 'demo_static/index.html')
