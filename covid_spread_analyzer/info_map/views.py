import jsonpickle as jsonpickle
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from firebase_admin import credentials

from covid_spread_analyzer.info_map.models import *
from firebase_files.fb_conf import *

from django.template import loader


########################################################################################################################
####################################################### views ##########################################################
########################################################################################################################

def map_view(request):
    template = loader.get_template('map.html')
    context = {"1": {
        "Dolnośląskie": 123,
        "Kujawsko-pomorskie": 10,
        "Lubelskie": 12,
        "Lubuskie": 132,
        "Łódzkie": 12,
        "Małopolskie": 350,
        "Mazowieckie": 11,
        "Opolskie": 123,
        "Podkarpackie": 1,
        "Podlaskie": 123,
        "Pomorskie": 1114,
        "Śląskie": 123,
        "Świętokrzyskie": 534,
        "Warmińsko-mazurskie": 342,
        "Wielkopolskie": 764,
        "Zachodniopomorskie": 90
    }, "2": {
        "Dolnośląskie": 10,
        "Kujawsko-pomorskie": 10,
        "Lubelskie": 10,
        "Lubuskie": 10,
        "Łódzkie": 10,
        "Małopolskie": 10,
        "Mazowieckie": 10,
        "Opolskie": 10,
        "Podkarpackie": 1,
        "Podlaskie": 10,
        "Pomorskie": 10,
        "Śląskie": 123,
        "Świętokrzyskie": 534,
        "Warmińsko-mazurskie": 342,
        "Wielkopolskie": 764,
        "Zachodniopomorskie": 90
    }}
    context = jsonpickle.encode(context)
    return render(request=request, template_name='map.html', context={"data": context})


'''
def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context=RequestContext(request))
    response.status_code = 404
    return response
'''
