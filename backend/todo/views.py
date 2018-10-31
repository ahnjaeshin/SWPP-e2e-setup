from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
import json
from json.decoder import JSONDecodeError


def index(request):
    return HttpResponse('Hello World!')


@csrf_exempt
def todo_list(request):
    # Session check 부분
    if request.method == 'GET':
        # todo_list_objects = Todo.objects.all()
        # todo_list = todo_list_objects.values()
        # serialized = json.dumps()
        # return JsonResponse(todo_list, safe=False)

        todo_all_list = [todo for todo in Todo.objects.all().values()]
        # .value()는 Python과 Javascript가 서로 인식할 수 있도록 common data type(json)로 바꾸는 것(이 방식을 serialization이라고 함)
        return JsonResponse(todo_all_list, safe=False)
        # python에서 제공하는 JsonResponse는 python의 dictionary를 json으로 변환함

    elif request.method == 'POST':
        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
            # json 형식으로 보냈을 것이라고 여기고 assume하는 것
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        todo = Todo(todo=todo_content)
        todo.save()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done
        }
        return JsonResponse(response_dict, status=201)  # created
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def todo_detail(request, todo_id):
    if request.method == 'GET':
        # Todo.objects.filter(id=) QuerySet ...안전해서 try catch 안써도 됨
        #filtered = Todo.objects.filter(id=)
        #filtered.count() == 0: error
        # get -> Object
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()
        response_dict = {
            'id': todo.id,
            'content': todo.content,
            'done': todo.done
        }
        return JsonResponse(response_dict)
    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        try:
            body = request.body.decode()
            todo_content = json.loads(body)['content']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        todo.name = todo_content
        todo.save()
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return HttpResponseNotFound()

        todo.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])


