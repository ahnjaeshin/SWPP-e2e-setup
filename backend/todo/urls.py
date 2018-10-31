from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.TodoList.as_view()),
    path('todo/<int:id>/', views.TodoItem.as_view()),
]
