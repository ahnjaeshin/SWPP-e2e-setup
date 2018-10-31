from django.http import HttpResponse
from .models import Todo
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def toDoList(request):
    allowedRequests = ['GET', 'POST']

    if request.method in allowedRequests:
        if request.method == 'GET':
            resp_json = [
                {"content": todo_item["content"],
                 "done": todo_item["done"]
                 } for todo_item in Todo.objects.all().values()
            ]
            return HttpResponse(json.dumps(resp_json))

        elif request.method == 'POST':
            req_data = json.loads(request.body.decode())

            content = req_data["content"]
            done = req_data["done"]

            new_item = Todo(content=content, done=done)
            new_item.save()

            return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def toDoSpecified(request, **kwargs):
    allowedRequests = ['GET', 'PUT', 'DELETE']
    item_id = kwargs['itemId']

    if request.method in allowedRequests:
        try:
            target_item = Todo.objects.get(id=item_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            resp_json = json.dumps(
                {"content": target_item.content, "done": target_item.done})
            return HttpResponse(resp_json)

        elif request.method == 'PUT':
            req_data = json.loads(request.body.decode())
            content = req_data['content']
            done = req_data['done']

            target_item.content = content
            target_item.done = done

            target_item.save()

            return HttpResponse(status=200)

        elif request.method == 'DELETE':
            target_item.delete()

            return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)
