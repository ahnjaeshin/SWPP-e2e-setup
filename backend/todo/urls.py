from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo_list, name = 'todo_list'),
    path('todo/<int:id>/', views.todo_detail ),
]
