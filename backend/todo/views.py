from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json
from django.views.decorators.csrf import csrf_exempt
from django.test import TestCase, Client
from todo.models import Todo
from django.db import models

def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        todo_all_list = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todo_all_list, safe=False)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        todo = Todo(content = content, done=done)
        todo.save()
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])    

@csrf_exempt
def edit(request, edit_id):
    if request.method == 'GET':
        target_todo = Todo.objects.filter(id=edit_id)
        if target_todo.exists(): 
            x = target_todo.values()[0]
            return JsonResponse(json.dumps(x), safe=False)
        else:
            return HttpResponse(status=404)
    elif request.method == 'PUT':
        target_todo = Todo.objects.filter(id=edit_id)
        if target_todo.exists():
            req_data = json.loads(request.body.decode())
            todo = target_todo[0]
            todo.content = req_data['content']
            todo.done = req_data['done']
            todo.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    elif request.method == 'DELETE':
        target_todo = Todo.objects.filter(id=edit_id)
        if target_todo.exists():
            todo = target_todo[0]
            todo.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
