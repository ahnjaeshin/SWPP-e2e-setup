from django.test import TestCase, Client
from .models import Todo
import json


class TodoTestCase(TestCase):

    def setUp(self):
        item1 = Todo(content="go to bed", done=False)
        item2 = Todo(content="wake up", done=True)

        item1.save()
        item2.save()

    def test_index(self):
        client = Client()
        response = client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello World!')

    def test_list(self):
        client = Client()

        # get
        response_get = client.get('/api/todo/')
        self.assertIsInstance(json.loads(response_get.content)[0], dict)

        # post
        response_post = client.post(
            '/api/todo/', {"content": "have breakfast", "done": "False"}, content_type="application/json")
        self.assertEqual(response_post.status_code, 201)

        # unallowed method (delete)
        response_delete = client.delete('/api/todo/')
        self.assertEqual(response_delete.status_code, 405)

    def test_todoSpecified(self):
        client = Client()

        # get
        response_get = client.get('/api/todo/1/')
        self.assertIsInstance(json.loads(response_get.content), dict)

        # put
        response_put = client.put(
            '/api/todo/1/', {"content": "modified task", "done": "False"}, content_type="application/json")
        self.assertEqual(response_put.status_code, 200)

        # delete
        response_delete = client.delete('/api/todo/1/')
        self.assertEqual(response_put.status_code, 200)

        # post (unallowed)
        response_post = client.post(
            '/api/todo/1/', {"something": "something"}, content_type="application/json")
        self.assertEqual(response_post.status_code, 405)
