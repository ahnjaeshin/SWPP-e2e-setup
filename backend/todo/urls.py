from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]
