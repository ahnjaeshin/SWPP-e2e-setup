from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todo/', todo_list),
    path('todo/<int:todo_id>/', todo_detail),
]
