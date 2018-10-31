from django.urls import include, path
from . import views


urlpatterns = [
    path('todo', views.article, name='todo'),
    path('todo/<int:id>', views.targetarticle, name='targettodo'),
]