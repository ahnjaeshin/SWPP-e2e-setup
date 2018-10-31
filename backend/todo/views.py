from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo


@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todo_list_objects = Todo.objects.all()
        todo_list = todo_list_objects.values()
        return JsonResponse(todo_list)

    elif request.method == 'POST':
        request.body.decode()
        pass

    else:
        return HttpResponseNoAllowed(['GET', "PUT", 'DELETE'])

@csrf_exempt
def todo_details(request,id):
    if request.method == 'GET':
        Todo.objects.filter(id)
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    else:
        pass
