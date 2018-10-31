from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import ToDo
import json
from json.decoder import JSONDecodeError


def index(request):
    return HttpResponse('Hello World!')

def todo_list(request):
    if request.method == 'GET':
        todo_all_list = [td for td in ToDo.objects.all().values()]
        return JsonResponse(todo_all_list, safe = False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            td_content = json.loads(body)['content']
            td_done = json.loads(body)['done']
            td_due = json.loads(body)['due']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        td = ToDo(content = td_content, done = td_done, due = td_due)
        td.save()
        response_dict = {
            'content' : td_content.
            'done' : td_done,
            'due' : td_due,
        }
        return JsonResponse(response_dict, status = 201)

def todo_int(request, id = ''):
