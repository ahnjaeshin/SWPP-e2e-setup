from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

class TodoTestCase(TestCase):
    def test_index(self):
        client = Client()
        response = client.get('/api/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'Hello World!')

class ViewTestCase(APITestCase):
    def test_ToDo_get(self):
        url = reverse('todo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ToDo_post(self):
        url = reverse('todo')
        data = {"content": "cont1" }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

     
    def create_todo(self, content):
        url = reverse('todo')
        data = {"content": content }
        response = self.client.post(url, data, format='json')
        return response

    def test_ToDoDetail_get(self):
        response = self.create_todo('cont1')
        url = reverse('todo_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ToDoDetail_put(self):
        response = self.create_todo('cont1')
        url = reverse('todo_detail', kwargs={'pk': 1})
        data = {"content": "cont2" }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ToDoDetail_delete(self):
        response = self.create_todo('cont1')
        url = reverse('todo_detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
