from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Todo


def index(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def todo(request, pk=None):
    if request.method == "POST":
        data = {
            'content' :request.data.get('content', ''),
            'done': request.data.get('done', False),
        }
        instance = Todo(**data)
        instance.save()
        return JsonResponse(
            {
                'content': instance.content,
                'done': instance.done,
                'due': instance.due
            }
        )

    elif request.method == "GET":
        if pk == None:
            queryset = Todo.objects.all()
            data = list(map(lambda x: {'content': x.content, 'done': x.done, 'due': x.due}, queryset))
            return HttpResponse(data)
        else:
            instance = get_object_or_404(Todo, pk=4)
            return JsonResponse(
                {
                    'content': instance.content,
                    'done': instance.done,
                    'due': instance.due
                }
            )
    elif request.method == "DELETE":
        instance = get_object_or_404(Todo, pk=4)
        instance.objects.delete()
        return HttpResponse("")


    elif request.method == "PUT":
        instance = get_object_or_404(Todo, pk=4)
        content = request.data.get('content', None)
        done = request.data.get('done', None)
        if content:
            instance.content = content
        if done:
            instance.done = done
        instance.save()
        return JsonResponse(
            {
                'content': instance.content,
                'done': instance.done,
                'due': instance.due
            }
        )

    else :
        return HttpResponse("bad request")
