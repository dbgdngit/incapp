from django.http import HttpResponse
from django.template import loader
import operator

from .models import INCIDENT

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def recent(request):
    recent_incident_list = INCIDENT.objects.order_by('-incref')
    template = loader.get_template('summary.html')
    context = {
        'recent_incident_list': recent_incident_list,
    }
    return HttpResponse(template.render(context, request))
