from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo


@csrf_exempt
def todos(request):
    if request.method == 'GET':
        todo_all = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todo_all, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo(content=content, done=done)
        todo.save()
        response_dict = {
            'id': todo.id,
            'name': todo.content,
            'done': todo.done,
        }
        return JsonResponse(response_dict, status=201)  # created
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])

@csrf_exempt
def todo(request, todo_id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done,
        }
        return JsonResponse(response_dict)
    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        try:
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        todo.content = content
        todo.done = done
        todo.save()
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        todo.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

