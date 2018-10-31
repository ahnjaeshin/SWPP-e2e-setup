from django.http import HttpResponse
from todo.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed

from django.http import HttpResponseBadRequest, HttpResponseNotFound

from django.views.decorators.csrf import csrf_exempt

import json

from json.decoder import JSONDecodeError

from .models import Todo

def index(request):
    if request.method == 'GET':
        raw = Todo.objects.all()
        rst = []
        for obj in raw:
            tmpdict={}
            tmpdict['content']=obj.content
            tmpdict['done']=obj.done
            rst.append(tmpdict)
#print(rst)
        return JsonResponse(rst,status=200,safe=False)
    elif request.method == 'POST':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        tod = Todo(content=content, done=done)
#create in db
        tod.save()
		
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['POST'])
@csrf_exempt
def config(request, number):
    if request.method == 'GET':
        tod = Todo.objects.all().filter(id=number).get()
        tmpdict={"content":tod.content,
    	"done":tod.done
		}
		#print(tmpdict)
        return JsonResponse(tmpdict,status=200)
    elif request.method == 'PUT':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        tod = Todo.objects.filter(id=number).get()
        tod.content = content
        tod.done = done
        tod.save()
        return HttpResponse(status=200)
    elif request.method == 'DELETE':
        req_data = json.loads(request.body.decode())
        content = req_data['content']
        done = req_data['done']
        tod = Todo.objects.filter(id=number).get()
        tod.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)