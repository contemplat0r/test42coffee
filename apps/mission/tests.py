from django.test import TestCase
from mission.models import PersonDescription

# Create your tests here.

class PersonDescriptionTestCase(TestCase):
    def setUp(self):
        PersonDescription.objects.create(name='Leonard', surname='Hofstadter', birthdate='1981-10-01', email='not.sheldon@gmail.com', phone='111111111', bio='Very long biography')
        PersonDescription.objects.create(name='Sheldon', surname='Cuper', birthdate='1981-10-02', email='sheldon___gmail.com', phone='222222222')
        PersonDescription.objects.create(name='W' * 34, surname='None', birthdate='1981-10-02', email='sheldon___gmail.com', phone='222222222')

    def test_model_data_correctness(self):
        correct_person_description = PersonDescription.objects.get(name='Leonard')
        self.assertEqual(correct_person_description.email.find('@') != -1, True)
        incorrect_person_description = PersonDescription.objects.get(name='Sheldon')
        self.assertEqual(incorrect_person_description.email.find('@') != -1, True)
        another_incorrect_person_description = PersonDescription.objects.get(surnmae='None')
        self.assertEqual(len(another_incorrect_person_description.name) < 33, True)
