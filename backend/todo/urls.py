from django.urls import include, path
from . import views


urlpatterns = [
    path('api/todo/', views.todos),
    path('api/todo/<int:id>/', views.todo)
]