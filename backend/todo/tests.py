from django.test import TestCase, Client
from .models import Todo
import json

class TodoTestCase(TestCase):
	def setUp(self):
		Todo.objects.create(content='task1', done=False)
		Todo.objects.create(content='task2', done=False)
		Todo.objects.create(content='task3', done=True)
		Todo.objects.create(content='task4', done=False)
		Todo.objects.create(content='task5', done=True)
		Todo.objects.create(content='task6', done=True)
		Todo.objects.create(content='task7', done=False)

	def test_index(self):
		client = Client()
		response = client.get('/api/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content.decode(), 'Hello World!')

	def test_todo(self):
		client = Client()

		response = client.put('/api/todo', json.dumps({'content': 'task', 'done': 'False'}),
								content_type='application/json')
		self.assertEqual(response.status_code, 405)

		response = client.delete('/api/todo')
		self.assertEqual(response.status_code, 405)

		response = client.get('/api/todo')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(Todo.objects.all()), 7)

		response = client.post('/api/todo', json.dumps({'content': 'task', 'done': 'False'}),
								content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_todo_id(self):
		client = Client()

		response = client.post('/api/todo/9', json.dumps({'content': 'task', 'done': 'False'}),
								content_type='application/json')
		self.assertEqual(response.status_code, 405)

		response = client.get('/api/todo/9')
		self.assertEqual(response.status_code, 404)

		response = client.get('/api/todo/1')
		response_data = json.loads(response.content.decode())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response_data['content'], 'task1')

		response = client.put('/api/todo/9', json.dumps({'content': 'task', 'done': 'True'}),
								content_type='application/json')
		self.assertEqual(response.status_code, 404)

		response = client.put('/api/todo/1', json.dumps({'content': 'task', 'done': 'True'}),
								content_type='application/json')
		self.assertEqual(response.status_code, 200)

		response = client.delete('/api/todo/9')
		self.assertEqual(response.status_code, 404)

		response = client.delete('/api/todo/1')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(Todo.objects.all()), 6)		