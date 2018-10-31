from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed

from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json

from json.decoder import JSONDecodeError
from .models import Todo


def index(request):
    return HttpResponse("Hello")

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todo_list_objects = Todo.objects.all()
        todo_list = todo_list.objects.values()
        return JsonResponse(todo_list, safe = False)

    elif request.method == 'POST':
        body = request.body.decode()
    else:
        return HttpResponseNotAllowed(['GET', 'PUT','DELETE'])


def todo_detail(request, id):
    if request.method == 'GET':
        Todo.objects.filter(id)

    elif request.method == 'PUT':
        pass
    
    elif request.method == 'DELETE':
        pass
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
