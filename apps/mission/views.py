# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    context = {'person_description': {
        'name': 'Nikolai',
        'second_name': 'Golikov',
        'birthdate': '1969-10-04',
        'biography': ' Very, very long biography\n' +
        '.' * 19 + '\n' + '.' * 19 + '\n' + 'Biography end.',
        'email': 'uldo.forme@gmail.com',
        'jabber_id': 'contemplat0r@42cc.co',
        'skype_id': 'contemplat0r',
        'other_contacts': 'Phone: +380507777777'}}
    return render_to_response('person.html', context)
