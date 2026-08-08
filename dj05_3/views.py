from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Profile


def index(request):
    return render(request, 'dj05_3/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()                       # 1) создаём СТАНДАРТНОГО User
            Profile.objects.create(                  # 2) заводим Profile сбоку (OneToOne)
                user=user,
                phone_number=form.cleaned_data.get('phone_number', ''),
            )
            return redirect('dj05_3:login')
    else:
        form = RegisterForm()
    return render(request, 'dj05_3/register.html', {'form': form})


@login_required(login_url='dj05_3:login')
def profile(request):
    return render(request, 'dj05_3/profile.html')
