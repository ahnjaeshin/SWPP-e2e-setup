from django.urls import include, path
from . import views


urlpatterns = [
    path('todo', views.todos, name='todos'),
    path('todo/<int:todo_id>', views.todo, name='todo'),
]
