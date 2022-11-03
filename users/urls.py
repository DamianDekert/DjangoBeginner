"""Wzorzec adresów URL dla aplikacji Users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #Strona rejestracji
    path('register/', views.register, name='register'),
]