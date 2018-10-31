from django.test import TestCase, Client
from .models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        client = Client()
        response = client.post('/api/todo/', {'content': 'AAAA'})
