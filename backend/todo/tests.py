from django.test import TestCase, Client


class TodoTestCase(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/api/')
        self.assertEqual(response.status_code, 404)