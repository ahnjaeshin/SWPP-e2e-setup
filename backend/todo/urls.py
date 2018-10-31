from django.urls import include, path
from . import views


urlpatterns = [
	path('todo/', views.todo_all, name="todo_all"),
]
