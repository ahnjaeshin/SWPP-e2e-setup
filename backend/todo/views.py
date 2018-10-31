from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo
from datetime import datetime

@csrf_exempt
def todo_all(request):
	if request.method == "GET":
		todo_all_list = [todo for todo in Todo.objects.all().values()]
		return JsonResponse(todo_all_list, safe=False)
	elif request.method == "POST":
		try:
			body = request.body.decode()
			print(body)
			js = json.loads(body)
			todo = Todo(id=1, content=js["content"], done=js["done"], due=datetime.now())
			todo.save()
		except:
			return HttpResponseBadRequest()
		d = {"id": 1, "content": todo.content, "done": todo.done, "due": todo.due}
		print(d)
		return JsonResponse(d, safe=False)
	return HttpResponse("Hello, world!")
