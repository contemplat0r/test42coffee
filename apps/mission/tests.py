from django.test import TestCase
from mission.models import PersonDescription

# Create your tests here.

class PersonDescriptionTestCase(TestCase):
    def setUp(self):
        PersonDescription.objects.create(name='Leonarg', surname='Hofstadter', birthdate='01-10-1981', email='not.sheldon@gmail.com', phone='111111111')
