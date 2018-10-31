import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo

def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todo_all_list = [hero for hero in Todo.objects.all().values()]
        return JsonResponse(todo_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo(content=content, done=done)
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done,
        }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@csrf_exempt
def todo_id(request, id=''):
    if request.method == 'GET':
        todom = Todo.objects.filter(id=id).values()[0]
        return JsonResponse(todom, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            content = json.loads(body)['content']
            done = json.loads(body)['done']
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo.objects.get(id=id)
        todo.content = content
        todo.done = done
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done,
        }
        return JsonResponse(response_dict, status=201)
    elif request.method == 'DELETE':
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({}, status=201)
    else:
        return HttpResponseNotAllowed(['GET','PUT','DELETE'])