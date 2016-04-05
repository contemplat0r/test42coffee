from django.test import TestCase
from django.test import Client
from mission.models import PersonDescription

# Create your tests here.


class ResponseDescriptionViewTest(TestCase):

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


class PersonDescriptionTestCase(TestCase):

    def setUp(self):
        PersonDescription.objects.create(
            name='Nikolai',
            surname='Golikov',
            birthdate='1969-10-04',
            bio='Very long biography\n' +
            '.' * 19 + '\n' + '.' * 19 + '\nBiography end.',
            email='uldo.forme@gmail.com',
            jabber='contemplat0r@42cc.co',
            skype='contemplat0r',
            other_contacts='Phone: +380507777777')

    def test_model_data_presence(self):

        '''
        Tests that check correct data presence in database
        '''

        person_description = PersonDescription.objects.get(name='Nikolai')
        self.assertEqual(person_description.surname, 'Golikov')
        self.assertEqual(person_description.skype, 'contemplat0r')
        self.assertEqual(person_description.email.find('@') != -1, True)

    def str_method(self):

        '''
        Check the correctness of str method.
        '''

        person_description = PersonDescription.objects.get(name='Nikolai')
        self.assertEqual(str(person_description), 'Nikolai Golikov')
