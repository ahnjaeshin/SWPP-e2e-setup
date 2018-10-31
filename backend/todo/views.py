from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

@csrf_exempt
def todos(request):
    if request.method == 'GET':
        todoList = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todoList, safe=False)
    elif request.method == 'POST':
        todo = json.loads(request.body.decode())
        content = todo['content']
        due = todo['due']
        done = todo['done']
        newTodo = Todo(content=content, due=due, done=done)
        newTodo.save()
        res = {
            'id': newTodo.id,
            'content': newTodo.content,
            'due': newTodo.due,
            'done': newTodo.done,
        }
        return JsonResponse(res, status=201)

@csrf_exempt
def todo(request, id=-1):
    if request.method == 'GET':
        todo = Todo.objects.get(id=id)
        return JsonResponse(todo)
    elif request.method == 'DELETE':
        Todo.objets.filter(id=id).delete()
        return JsonResponse(status=202)
    elif request.method == 'PUT':
        todo = json.loads(request.body.decode())
        todoObj = Todo.objects.get(id=todo.id)
        todoObj.content = todo['content']
        todoObj.due = todo['due']
        todoObj.done = todo['done']
        todoObj.save()
        return JsonResponse(status=204)


