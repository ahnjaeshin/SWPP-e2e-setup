from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        todos = Todo.objects.all().values('content','done')
        todos = json.dumps(list(todos))
        return HttpResponse(todos)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        Todo.objects.create(content = content)
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['Get','POST'])
@csrf_exempt
def todoDetail(request,todoID):
    if request.method == 'GET':
        todo = Todo.objects.filter(id=todoID)
        if len(todo) == 0:
                return HttpResponse(status=404)
        todo = todo.values()[0]
        return JsonResponse(todo)
    elif request.method == 'PUT':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        todo = Todo.objects.filter(id=todoID)
        if len(todo) == 0:
            return HttpResponse(status=404)
        todo[0].content = content
        todo[0].done = done
        todo[0].save()
        return HttpResponse(status=200)
    elif request.method == 'DELETE':
        todo = Todo.objects.filter(id=todoID)
        if len(todo) == 0:
            return HttpResponse(status=404)
        todo[0].delete()
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['Get','PUT','DELETE'])