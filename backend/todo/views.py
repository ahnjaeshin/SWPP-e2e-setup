from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed

from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json

from json.decoder import JSONDecodeError
from .models import Todo


def index(request):
    return HttpResponse("Hello")

def todo_list(request):
    if request.method == 'GET':
        todo_all_list = [todo for todo in Todo.objects.all().values()]
        return JsonResponse(todo_all_list, safe = False)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
