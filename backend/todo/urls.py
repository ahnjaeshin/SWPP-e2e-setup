from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo_list, name = 'todo_list'),
]
