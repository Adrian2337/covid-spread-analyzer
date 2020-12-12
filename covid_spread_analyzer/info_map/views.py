import jsonpickle as jsonpickle
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from firebase_admin import credentials

from covid_spread_analyzer.database_operations import load_data
from covid_spread_analyzer.info_map.models import *
from firebase_files.fb_conf import *

from django.template import loader


########################################################################################################################
####################################################### views ##########################################################
########################################################################################################################

def map_view(request):
    map_data = load_data('Map Data')
    dates = list(map_data.keys())[::-1]
    voivodes = load_data('Voivodeships')
    return render(request=request, template_name='map.html',
                  context={"map_data": map_data, "dates": dates ,"voivodes": voivodes})


def statistics_view(request, voivode):
    data = load_data('Voivodeships', voivode) if voivode != 'Polska' else load_data('Poland')
    return render(request=request, template_name='statistics.html', context={"data": data})
