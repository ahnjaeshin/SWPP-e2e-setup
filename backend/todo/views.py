from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo


@csrf_exempt
def todo(request: HttpRequest):
    if request.method not in ['GET', 'POST']:
        return HttpResponseNotAllowed(['GET', 'POST'])

    if request.method == 'GET':
        return JsonResponse(list(Todo.objects.all().values()), safe=False)
    else:
        try:
            body = json.loads(request.body.decode())
            content = body['content']
            done = body['done']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()

        todo = Todo(content=content, done=done)
        todo.save()

        return HttpResponse(status=201)


@csrf_exempt
def todo_detail(request: HttpRequest, todo_id=-1):
    if request.method == 'POST':
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return HttpResponseNotFound()

    if request.method == 'GET':
        return JsonResponse({'content': todo.content, 'done': todo.done}, safe=False)
    elif request.method == 'PUT':
        try:
            body = json.loads(request.body.decode())
            content = body['content']
            done = body['done']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()

        todo.content = content
        todo.done = done
        todo.save()

        return HttpResponse(status=200)
    else:
        todo.delete()

        return HttpResponse(status=200)
