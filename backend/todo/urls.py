from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/<int:todoID>', views.todoDetail, name='todo2'),
]