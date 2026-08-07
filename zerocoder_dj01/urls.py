"""
URL configuration for zerocoder_dj01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('dj01/', include('dj01.urls')),
    path('dj02/', include('dj02.urls')),
    path('dj03/', include('dj03.urls')),
    path('dj04/', include('dj04.urls')),
    path('demo/', include('demo.urls')),          # раздел «Демо» (хаб) — только ветка demo
    path('demo/for/', include('demo_for.urls')),  # демка про {% for %} — только ветка demo
    path('demo/static/', include('demo_static.urls')),  # демка про static — только ветка demo
]
