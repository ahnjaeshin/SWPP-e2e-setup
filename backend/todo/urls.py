from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/<int:id>/', views.todo_id, name='todo_id'),
    
]