from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Todo
import json

def todos(request):
    if request.method == 'GET':
        # return JsonResponse(Todo.objects.all().values(), safe = False)
        response = serialize("json",Todo.objects.all())
        return HttpResponse(response, content_type = 'application/json', status = 200)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        new_todo = Todo(content = content, done = False)
        new_todo.save()
        return HttpResponse(status = 201)

def todo_detail(request, todo_id):
    if request.method == 'GET':
        obj = Todo.objects.get(pk = todo_id)
        data = serialize("json", [obj,])
        struct = json.loads(data)
        response = struct[0]
        return HttpResponse(response, content_type = 'application/json', status = 200)
    elif request.method == 'DELETE':
        Todo.objects.filter(pk = todo_id).delete()
        return HttpResponse(status = 200)
    elif request.method == 'PUT':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        Todo.objects.filter(pk = todo_id).update(content = content)
        return HttpResponse(status = 200)
