from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo


@csrf_exempt
def todo_list(request):
    # Session Check
    if request.method == 'GET':
        todo_all_list = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todo_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo(content=todo_content)
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
        }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def todo_detail(request, id=''):
    if request.method == 'GET':
        todo = Todo.objects.filter(id=id).value()
        return JsonResponse(todo)
    elif request.method == 'DELETE':
        todo_all_list = [Todo.objects.exclude(id=id).values()]
        return JsonResponse(todo_all_list, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            todo_done = json.loads(body)['done']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo.objects.filter(id=id).value()
        todo.done = todo_done
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
        }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])

