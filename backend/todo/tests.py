from django.test import TestCase, Client
from .models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(content='Not easy, I think...')

    def test_index(self):
        client = Client()
        response = client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello World!')

    def test_todo_id(self):
        client = Client()
        response = client.get('/todo/3/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('3', response.content.decode())

    def test_todo(self):
        client = Client()

        response = client.get('/todo/')
        self.assertIn('1', response.content.decode())



