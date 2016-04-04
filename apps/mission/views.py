# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    context = {'person_description': {
        'name': 'Name',
        'second_name': 'Last name',
        'birthdate': 'Date of birth',
        'biography': 'Bio:',
        'email': 'email',
        'jabber_id': 'JID',
        'skype_id': 'id',
        'other_contacts': 'Other contacts'}}
    return render_to_response('person.html', context)
