from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def todo(request):

    # Session check

    if request.method == 'GET':
        todoes = list(Todo.objects.all().values())
        return JsonResponse(todoes, safe=False)

    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        due = req_data['due']
        
        todo.content = content
        todo.done = done
        todo.due = due
        todo.save()
        return HttpResponse(status=200)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
    
    
def todoDetail(request, todo_id):
    try:
        todo = todo.objects.get(id=todo_id)
    except todo.DoesNotExist:
        return HttpResponseNotFound()

    if request.method == 'GET':
        return JsonResponse(todo)

    elif request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=200)

    elif request.method == 'PUT':
        req.data = json.loads(request.body.decode())
        content = req_data['content']
        due = req_data['due']

        todo.content = content
        todo.due = due
        todo.save()
        return HttpResponse(status=200)

    else:
        return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])
