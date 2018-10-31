from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<int:id>/', views.todo_id, name='todo_id'),
    path('todo/', views.todo_list, name='todo_list'),
]