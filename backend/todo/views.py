from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from .models import Todo

def todo(request):
    if request.method == 'GET':
        return JsonResponse(Todo.objects.all().values(), safe=False)

    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        due = req_data['due']

        Todo(content=content, done=done, due=due).save()
        return HttpResponse(status=200)

    else:
        return HttpResponseNotAllowed(['GET','POST'])
def todo_id(request, id='id'):
    if request.method == 'GET':
        return JsonResponse(Todo.objects.filter(id=id))
    elif request.method == 'DELETE':
        Todo.objects.filter(id=id).delete()
        return HttpResponse(status=100)
    elif request.method == 'PUT':
        req_data = json.loads(request.body.decode())
        todo = Todo.objects.get(id=id)
        todo.content = req_data['content']
        todo.done = req_data['done']
        todo.due = req_data['due']
        return HttpResponse(status=100)        
    else:
        return HttpResponseNotAllowed(['GET','DELETE','PUT'])