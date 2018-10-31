from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Todo

def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo(request):

	if request.method == 'GET':
		todos = []
		for todo in Todo.objects.all():
			todo_dict = {}
			todo_dict['content'] = todo.content
			todo_dict['done'] = todo.done
			todos.append(todo_dict)
		return JsonResponse(todos, safe=False, status=200)

	elif request.method == 'POST':
		req_data = json.loads(request.body.decode())
		content = req_data['content']
		done = req_data['done']
		new_todo = Todo(content=content, done=done)
		new_todo.save()
		return HttpResponse(status=201)

	else:
		return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def todo_id(request, **kwargs):
	todo_queryset = Todo.objects.filter(id = kwargs['todo_id'])

	if request.method == 'GET':

		if len(todo_queryset) is 0:
			return HttpResponseNotFound('Not Found')

		todo = todo_queryset[0]
		todo_dict = {}
		todo_dict['content'] = todo.content
		todo_dict['done'] = todo.done
		return JsonResponse(todo_dict, status=200)

	elif request.method == 'PUT':

		if len(todo_queryset) is 0:
			return HttpResponseNotFound('Not Found')

		todo = todo_queryset[0]
		req_data = json.loads(request.body.decode())		
		
		todo.content = req_data['content']
		todo.done = req_data['done']
		todo.save()
		return HttpResponse(status=200)

	elif request.method == 'DELETE':

		if len(todo_queryset) is 0:
			return HttpResponseNotFound('Not Found')

		todo = todo_queryset[0]
		todo.delete()
		return HttpResponse(status=200)

	else:
		return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])