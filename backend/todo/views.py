from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        t_list = [T for T in Todo.objects.all().values()]
        return JsonResponse(t_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo_item = Todo(content=todo_content, done=False)
        todo_item.save()
        response_dict = {
            'id': todo_item.id,
            'content': todo_item.content,
            'done': todo_item.done,
        }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def todo(request, id):
    if request.method == 'GET':
        filtered = Todo.objects.filter(id=id)
        if filtered.count() == 0:
            return HttpResponse(status=404)
        f_list = [T for T in filtered.values()]
        return JsonResponse(f_list[0], safe=False)
    elif request.method == 'DELETE':
        Todo.objects.filter(id=id).delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
            done = json.loads(body)['done']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        Todo.objects.filter(id=id).update(content=todo_content, done=done)
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])