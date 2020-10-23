import random

import firebase_admin
from django.http import HttpResponse
from django.shortcuts import render
from firebase_admin import credentials

from covid_spread_analyzer.info_map.models import *
from firebase_files.fb_conf import *

from django.template import loader


########################################################################################################################
####################################################### views ##########################################################
########################################################################################################################

def map_view(request):
    template = loader.get_template('map.html')
    response_body = template.render({'current_user': request.user})

    return HttpResponse(response_body)
