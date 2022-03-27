from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('<int:blog_id>/', views.read, name='detail'),
    path('details/<int:blog_id>/', views.read, name='details'),
]