from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

@csrf_exempt
def todo(request):
    #request와 상관없는 session check같은 것들은 여기에 들어감.
    if request.method == 'GET':
        todo_list_objects = Todo.objects.all()
        todo_list = todo_list_objects.values()
        return JsonResponse(todo_list, safe=False)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        new_todo = Todo(content=content, done=false)
        new_todo.save()

    else:
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def todo(request, id):
    if request.method == 'GET':
        todo = Todo.objects.get(id=id)
        return JsonResponse({
            'content': todo.content,
            'done': todo.done,
            'due': todo.due
        })
    elif request.method == 'PUT':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        due = req_data['due']
        try:
            todo = Todo.objects.get(id=id)
            todo.content = content
            todo.done = done
            todo.due = due
            todo.save()
            return HttpREsponse(status=200)
        except:
            return HttpResponse(status=404)
    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
        except:
            return HttpREsponse(status=404)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
