from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/login', views.login, name='login'),
]
