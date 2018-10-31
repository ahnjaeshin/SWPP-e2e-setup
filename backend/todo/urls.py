from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.toDoList, name='todo-list'),
    path('todo/<int:itemId>/', views.toDoSpecified, name='todo-specified')
]
