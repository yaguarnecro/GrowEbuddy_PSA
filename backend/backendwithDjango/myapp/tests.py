from django.test import TestCase
from django.urls import reverse

class HelloWorldAPITests(TestCase):
    def test_hello_api(self):
        response = self.client.get(reverse('hello_api'))  # Use the name defined in urls.py
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Hello, World!"})
