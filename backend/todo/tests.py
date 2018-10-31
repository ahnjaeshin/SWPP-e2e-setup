from django.test import TestCase, Client
from todo.models import Todo

class TodoTestCase(TestCase):

    def setUp(self):
        Todo.objects.create(id = 1, content = '1')

    def test_index(self):
        client = Client()
        response = client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello World!')

    def test_todo_get(self):
        client = Client()
        response = client.get('/api/todo')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), '[{"id": 1, "content": "1", "done": false}]')

    def test_todo_post(self):
        client = Client()
        response = client.post('/api/todo')

        self.assertIn({'id': 1, 'content': "1", "done": True}, response.content.decode())
        self.assertEqual(response.status_code, 201)

    def test_todo_put(self):
        client = Client()
        response = client.put('/api/todo')

        self.assertEqual(response.status_code, 405)

    def test_todo_delete(self):
        client = Client()
        response = client.delete('/api/todo')

        self.assertEqual(response.status_code, 405)
    
    def test_edit_get_true(self):
        client = Client()
        response = client.get('/api/todo/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), '"{\\"id\\": 1, \\"content\\": \\"1\\", \\"done\\": false}"')
    
    def test_edit_get_false(self):
        client = Client()
        response = client.get('/api/todo/2')

        self.assertEqual(response.status_code, 404)
    
    def test_edit_delete_true(self):
        client = Client()
        response = client.delete('/api/todo/1')

        self.assertEqual(response.status_code, 200)

    def test_edit_delete_false(self):
        client = Client()
        response = client.delete('/api/todo/2')

        self.assertEqual(response.status_code, 404)
    
    def test_edit_put_true(self):
        client = Client()
        response = client.put('/api/todo/1')

        self.assertEqual(response.status_code, 200)

    def test_edit_put_false(self):
        client = Client()
        response = client.put('/api/todo/2')

        self.assertEqual(response.status_code, 404)
    
    def test_edit_post(self):
        client = Client()
        response = client.post('/api/todo/1')

        self.assertEqual(response.status_code, 405)
    
