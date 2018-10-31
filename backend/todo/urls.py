from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/todo/', views.todo_list),
    path('/todo/<int:todo_id>/', views.todo_detail),
]
