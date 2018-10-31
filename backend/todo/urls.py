from django.urls import include, path
from . import views

todo = views.ToDo.as_view({
	'get': 'list',
	'post': 'create',
})

todo_detail = views.ToDoDetail.as_view({
	'get': 'retrieve',
	'delete': 'destroy',
	'put': 'update',
})

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', todo, name='todo'),
    path('todo/<int:pk>', todo_detail, name='todo_detail'),
]