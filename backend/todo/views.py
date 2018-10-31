from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

@csrf_exempt
def todo_list(request):
    # Sessino check
    if request.method == 'GET':
        todo_list_objects = Todo.objects.all()
        todo_list = todo_list_objects.values() 
        return JsonResponse(todo_list, safe=False)
    elif requst.method == 'POST':
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest
        todo = Todo(content=todo_content)
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
        }
        return JsonResponse(response_dict, status=201) # created
    else:
        return HttpRequestNotAllowed(['GET', 'POST'])

@csrf_exempt
def todo_detail(request, todo_id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
        }
        return JsonResponse(response_dict)
    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        try:
            body = request.body.decode()
            todo.content = json.loads(body)['content']
            todo.done = json.loads(body)['done']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest

        todo.save()
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound

        todo.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET','PUT','DELETE'])
        
