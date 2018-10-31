from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
import json
from json.decoder import JSONDecodeError


@csrf_exempt
def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo(request):
    if (request.method == "GET"):
        todo_object_list = Todo.objects.all()
        todo_list = todo_object_list.values()
        return JsonResponse(todo_list, safe=False)

    elif (request.method == "POST"):
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
            todo_due = json.loads(body)['due']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        t = Todo(content=todo_content, due=todo_due)
        response_dict = {
            'id': t.id,
            'content': t.content,
            'due': t.due,
        }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def detail(request, id):
    if (request.method == "GET"):
        Todo.objects.filter()
        pass

    elif (request.method == "DELETE"):
        pass

    elif (request.method == "PUT"):
        pass
    else:
        pass
