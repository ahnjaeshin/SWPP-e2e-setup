from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo


def todo_list(request):
	if request.method == "GET":
		todo_list_objects = Todo.objects.all()
		todo_list = todo_list_objects.values()
		return JsonResponse(todo_list, safe=False)
	elif request.method == "POST":
		request.body.decode()
		Todo(content done)
	else: