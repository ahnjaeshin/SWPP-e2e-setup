from django.urls import include, path
from . import views


urlpatterns = [
    path('todo', views.todos),
    path('todo/<int:todo_id>', views.todo_detail),
]