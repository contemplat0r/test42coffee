from django.test import TestCase
from django.test import Client

# Create your tests here.


class ResponseDescriptionViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_response(self):
        '''
        Simple tests that check response HTTP code correctnes,
        right template presence, and presence some string in rendered html.
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person.html')
        self.assertContains(response, 'class="container"')
