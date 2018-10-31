from django.test import TestCase, Client
import json

class TodoTestCase(TestCase):
    def setUp(self):
        client = Client()
        client.post('/api/todo', json.dumps({'content': 'todo1'}), content_type='application/json')
        client.post('/api/todo', json.dumps({'content': 'todo2'}), content_type='application/json')
        client.post('/api/todo', json.dumps({'content': 'todo3'}), content_type='application/json')
        client.post('/api/todo', json.dumps({'content': 'todo4'}), content_type='application/json')
    def test_todos(self):
        client = Client()
        response = client.get('/api/todo')
        self.assertEqual(response.status_code, 200)
        response =client.post('/api/todo', json.dumps({'content': 'new_todo'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    def test_todo_detail(self):
        client = Client()
        response = client.get('/api/todo/1')
        self.assertEqual(response.status_code, 200)
        response = client.put('/api/todo/1', json.dumps({'content': 'changed_todo'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = client.delete('/api/todo/1')
        self.assertEqual(response.status_code, 200)
