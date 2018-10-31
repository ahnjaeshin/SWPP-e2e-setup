from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from json.decoder import JSONDecodeError
from .models import Todo

class BaseTodo(View):
    def represent(self, todo: Todo):
        return {
            "id": todo.id,
            "done": todo.done,
            "content": todo.content,
        }
    
    def build_up(self, request):
        params = json.loads(request.body)
        return dict(
            id=params.get('id', None),
            done=params['done'],
            content=params['content'],
        )
    

class TodoList(BaseTodo):
    def get(self, request):
        return JsonResponse([
            self.represent(todo)
            for todo in Todo.objects.order_by('id').all()
        ], safe=False)

    @csrf_exempt
    def post(self, request):
        todo = Todo(**self.build_up(request))
        todo.save()
        return JsonResponse(self.represent(todo))


class TodoItem(BaseTodo):
    def get(self, request, id):
        try:
            return JsonResponse(self.represent(Todo.objects.get(pk=id)))
        except Todo.DoesNotExist:
            return JsonResponse({}, status=404)

    @csrf_exempt
    def put(self, request, id):
        todo = Todo.objects.get(pk=id)

        d = self.build_up(request)
        d.pop('id', None)
        for attr, value in d.items():
            setattr(todo, attr, value)
        todo.save()
        return JsonResponse(self.represent(todo))

    @csrf_exempt
    def delete(self, request, id):
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return JsonResponse(self.represent(todo))

