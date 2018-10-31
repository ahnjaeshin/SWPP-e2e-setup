from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

def todo(request):
    if request.method == 'GET':
        todoList = [t for t in Todo.objects.all().values()]
        return JsonResponse(todoList, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
            due = json.loads(body)['due']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo(
                content = content,
                done = done,
                due = due,
            )
        todo.save()
        responseDict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done,
            'due': todo.due,

        }
        return JsonResponse(response_dict)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def singleTodo(request, todo_id):
    if request.method == 'GET':
        todoList = [t for t in Todo.objects.filter(id=todo_id).values()]
        return JsonResponse(todoList, safe=False)

    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()
        
        try: 
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
            due = json.loads(body)['due']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        
        todo.content = content
        todo.done = done
        todo.due = due
        return HttpResponse(status=204)

    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=article_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        todo.delete()
        return HttpResponseNotFound()
        
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])