# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from apps.mission.models import PersonDescription

# Create your views here.


def home(request):
    context = {'person_description': None}
    try:
        person_description = PersonDescription.objects.get(
            email='uldo.forme@gmail.com'
        )
    except PersonDescription.DoesNotExist:
        person_description = None

    if person_description is not None:
        context = {
            'person_description': {
                'name': person_description.name,
                'second_name': person_description.surname,
                'birthdate': person_description.birthdate,
                'biography': person_description.bio,
                'email': person_description.email,
                'jabber_id': person_description.jabber,
                'skype_id': person_description.skype,
                'other_contacts': person_description.other_contacts
            }
        }
    return render_to_response('person.html', context)
