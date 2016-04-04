from django.test import TestCase
from django.test import Client
from mission.models import PersonDescription

# Create your tests here.


class ResponseDescriptionViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person.html')
        self.assertContains(response, 'class="container"')

