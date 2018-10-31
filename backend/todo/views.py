from django.http import HttpResponse
from django.core import serializers
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        data = serializers.serialize('json', Todo.objects.all().values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        due = req_data['boolean']
        new_todo = Todo(content=content, done=done, due=due)
        new_todo.save()
        return HttpResponse(status=200)

@csrf_exempt
def todoN(request, id):
    if request.method == 'GET':
        row = Todo.objects.filter(id=id)
        return JsonResponse(serializers.serialize('json', row), safe=False)
    elif request.method == 'DELETE':
        row = Todo.objects.filter(id=id)
        row.delete()
        return HttpResponse(status=200)
    elif request.method == 'PUT':
        row = Todo.objects.filter(id=id)
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        due = req_data['boolean']
        row.content = content
        row.done = done
        row.due = due
        row.save()
        return HttpResponse(status=200)
