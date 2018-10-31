from django.urls import include, path
from todo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo', views.todo, name='todo'),
    path('todo/<int:edit_id>', views.edit, name='id')
]
