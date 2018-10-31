from django.test import TestCase, Client
from .models import Todo
import datetime
import json

class TodoTestCase(TestCase):

    def setUp(self):
        todo = Todo(content='content1', done=False)
        todo.save()

    def test_todo(self):
        client = Client()
        response = client.get('/api/todo/')
        self.assertIn('content1', response.content.decode())

        response = client.post('/api/todo/', json.dumps({'content': 'content2', 'done': False}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
