from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:todo_id>', views.todo_id, name='todo_id')
]