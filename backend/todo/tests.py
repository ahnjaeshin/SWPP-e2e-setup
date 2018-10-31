from django.test import TestCase, Client
from .models import Todo
import json

class TodoTestCase(TestCase):
    def setUp(self):
        todo1 = Todo.objects.create(content="hw1", done=False)
        todo2 = Todo.objects.create(content="hw2", done=True)

    def test_list(self):
        client = Client()
        response = client.get('/api/todo')
        self.assertEqual(response.status_code, 200)
        todos = json.loads(response.content)
        self.assertEqual(len(todos), 2)

    def test_todo_create(self):
        client = Client()
        response = client.post('/api/todo', json.dumps({'content': 'hwhw', 'done': 'True'}),
                content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = client.post('/api/todo', json.dumps({'test': "test"}),
                content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_todo_detail(self):
        client = Client()
        response = client.get('/api/todo/1')
        self.assertEqual(response.status_code, 200)
        todo = json.loads(response.content)
        self.assertEqual(todo.get("content"), "hw1")
        self.assertEqual(todo.get("done"), False)

        response = client.get('/api/todo/100')
        self.assertEqual(response.status_code, 404)

    def test_todo_delete(self):
        client = Client()
        response = client.delete('/api/todo/1')
        self.assertEqual(response.status_code, 204)

        response = client.delete('/api/todo/100')
        self.assertEqual(response.status_code, 404)

    def test_todo_put(self):
        client = Client()
        response = client.put('/api/todo/1', json.dumps({'content': 'hwhw2222', 'done': True}),
                content_type='application/json')
        self.assertEqual(response.status_code, 204)

        response = client.put('/api/todo/1', json.dumps({'test': 'hwhw2222'}),
                content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response = client.put('/api/todo/100', json.dumps({'content': 'hwhw2222', 'done': True}),
                content_type='application/json')
        self.assertEqual(response.status_code, 404)




