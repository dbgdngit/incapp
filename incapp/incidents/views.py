from django.http import HttpResponse
from django.template import loader
import operator

#..
from django.conf import settings
from django.shortcuts import redirect
#..


from .models import INCIDENT

def index(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))

def recent(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    recent_incident_list = INCIDENT.objects.order_by('-incref')
    template = loader.get_template('summary.html')
    context = {
        'recent_incident_list': recent_incident_list,
    }
    return HttpResponse(template.render(context, request))
