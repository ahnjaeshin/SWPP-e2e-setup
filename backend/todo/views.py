from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo
from datetime import datetime

@csrf_exempt
def todo(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        todos = [{'id': todo.id,
                  'content': todo.content,
                  'done': todo.done} for todo in Todo.objects.all()]
        return HttpResponse(json.dumps(todos),
                            content_type='application/json',
                            status=200)

    else: # POST
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        due = datetime.now()
        newTodo = Todo(content=content, done=False, due=due)
        newTodo.save()
        newTodo = {
            'id': newTodo.id,
            'content': newTodo.content,
            'done': newTodo.done
        }
        return HttpResponse(json.dumps(newTodo),
                            content_type='application/json',
                            status=200)


@csrf_exempt
def todoById(request, **kwargs):
    if request.method not in ['GET', 'PUT', 'DELETE']:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

    todoId = kwargs['todo_id']
    try:
        todo = Todo.objects.get(id=todoId)
    except Todo.DoesNotExist:
        return HttpResponseNotFound

    if request.method == 'GET':
        todo = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done
        }
        return HttpResponse(json.dumps(todo),
                            content_type='application/json',
                            status=200)
    if request.method == 'PUT':
        todo.done = not todo.done
        todo.save()
        return HttpResponse(status=200)
    else: # DELETE
        Todo.objects.filter(id=todoId).delete()
        return HttpResponse(status=200)