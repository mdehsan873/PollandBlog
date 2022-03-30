from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('pages/home',views.index,name='home'),
    path('pages/signup', views.signup, name='signup'),
]
