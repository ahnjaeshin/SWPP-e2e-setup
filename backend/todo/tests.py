import json

from django.test import TestCase, Client

class TodoTestCase(TestCase):
    def test_put_get_update_delete(self):
        client = Client()

        response = client.post('/api/todo/', json.dumps({"content": "HELLO", "done": False}), content_type="application/json")
        self.assertEqual(response.json()["content"], "HELLO")
        self.assertEqual(response.json()["done"], False)

        response = client.get('/api/todo/')
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["content"], "HELLO")
        self.assertEqual(response.json()[0]["done"], False)

        id = response.json()[0]["id"]

        response = client.get(f'/api/todo/{id}/')
        self.assertEqual(response.json()["content"], "HELLO")
        self.assertEqual(response.json()["done"], False)

        response = client.put(f'/api/todo/{id}/', json.dumps({"content": "HELLO", "done": True}), content_type="application/json")
        self.assertEqual(response.json()["done"], True)

        response = client.get(f'/api/todo/{id}/')
        self.assertEqual(response.json()["content"], "HELLO")
        self.assertEqual(response.json()["done"], True)

        response = client.delete(f'/api/todo/{id}/')
        self.assertEqual(response.status_code, 200)

        response = client.get(f'/api/todo/{id}/')
        self.assertEqual(response.status_code, 404)

