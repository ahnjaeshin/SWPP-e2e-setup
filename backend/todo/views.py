from rest_framework import viewsets

from django.http import HttpResponse
from .models import Todo
from .serializers import ToDoSerializer


def index(request):
    return HttpResponse('Hello World!')

class ToDo(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetail(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

