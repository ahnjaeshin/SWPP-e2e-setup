from django.http import HttpResponse, JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        todo_list = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todo_list, safe=False)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        todo = Todo(content=req_data['content'], done=req_data['done'])
        todo.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def todoid(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
            response = {
                'id': todo.id,
                'content': todo.content,
                'done': todo.done,
            }
            return JsonResponse(response, safe=False)
        except:
            return HttpResponse(status=404)
    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=404)
    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=id)
            if todo.done == True:
                todo.done = False
            else:
                todo.done = True
            todo.save()

            print(todo.done)
            response = {
                'id': todo.id,
                'content': todo.content,
                'done': todo.done,
            }
            return JsonResponse(response, safe=False)
        except:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)
