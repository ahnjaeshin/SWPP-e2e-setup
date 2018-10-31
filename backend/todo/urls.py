from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo_list),
    path('todo/<int>/', views.todo_details)
]
