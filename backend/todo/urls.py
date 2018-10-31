from django.urls import include, path
from . import views


urlpatterns = [
    path('todo/', views.),
    path('todo/<int:id>', views.),
]