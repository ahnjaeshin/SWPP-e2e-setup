from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo_list, name='todo list'),
    path('todo/<int:todo_id>/', views.todo_detail, name='todo detail'),
]