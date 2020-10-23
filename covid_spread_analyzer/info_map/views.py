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
    response_body = template.render({'current_user': request.user})
    return HttpResponse(response_body)


'''
def handler404(request, *args, **argv):
    response = render('404.html', {},
                      context=RequestContext(request))
    response.status_code = 404
    return response
'''
