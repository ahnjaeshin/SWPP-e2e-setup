from django.test import TestCase, Client
import json
from .models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.todo = Todo(content="foo", done=False)
        self.todo.save()

    def get(self, url):
        return self.client.get(url)

    def post(self, url, obj):
        return self.client.post(url, json.dumps(obj), content_type='application/json')

    def put(self, url, obj):
        return self.client.put(url, json.dumps(obj), content_type='application/json')

    def delete(self, url):
        return self.client.delete(url)

    def test_get_todo(self):
        resp = self.get('/api/todo/')
        self.assertEqual(resp.status_code, 200)

        resp_json = resp.json()
        self.assertEqual(len(resp_json), 1)
        self.assertEqual(resp_json[0]['content'], self.todo.content)
        self.assertEqual(resp_json[0]['done'], self.todo.done)

    def test_post_todo(self):
        new_todo = {'content': 'bar', 'done': True}
        resp = self.post('/api/todo/', new_todo)
        self.assertEqual(resp.status_code, 201)

        all_todos = Todo.objects.all()
        todo = all_todos[len(all_todos) - 1]
        self.assertEqual(todo.content, new_todo['content'])
        self.assertEqual(todo.done, new_todo['done'])

    def test_get_todo_detail(self):
        resp = self.get('/api/todo/{}/'.format(self.todo.id))
        self.assertEqual(resp.status_code, 200)

        resp_json = resp.json()
        self.assertEqual(resp_json['content'], self.todo.content)
        self.assertEqual(resp_json['done'], self.todo.done)

    def test_put_todo_detail(self):
        id = self.todo.id
        new_todo = {'content': 'bar', 'done': True}
        resp = self.put('/api/todo/{}/'.format(id), new_todo)
        self.assertEqual(resp.status_code, 200)

        todo = Todo.objects.get(id=id)
        self.assertEqual(todo.content, new_todo['content'])
        self.assertEqual(todo.done, new_todo['done'])

    def test_delete_todo_detail(self):
        id = self.todo.id
        resp = self.delete('/api/todo/{}/'.format(id))
        self.assertEqual(resp.status_code, 200)

        todos = Todo.objects.filter(id=id)
        self.assertTrue(not todos.exists())

    def test_not_allowd(self):
        self.assertEqual(self.put('/api/todo/', {}).status_code, 405)
        self.assertEqual(self.delete('/api/todo/').status_code, 405)

        self.assertEqual(self.post('/api/todo/0/', {}).status_code, 405)

    def test_bad_request(self):
        self.assertEqual(self.post('/api/todo/', {}).status_code, 400)

        self.assertEqual(
            self.put('/api/todo/{}/'.format(self.todo.id), {}).status_code, 400)

    def test_not_found(self):
        self.assertEqual(self.get('/api/todo/0/').status_code, 404)
        self.assertEqual(self.put('/api/todo/0/', {}).status_code, 404)
        self.assertEqual(self.delete('/api/todo/0/').status_code, 404)
