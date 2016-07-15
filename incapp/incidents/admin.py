from django.contrib import admin

from .models import (INCIDENT,INCIDENTSADMIN,INC_REPORTED_METHOD,
INC_TYPE,INC_IMPACT,INC_SEVERITY,INC_RESPONSE,INC_REMEDIAL,INC_ROOT_CAUSE,
INC_REMEDIALADMIN)

admin.site.register(INCIDENT,INCIDENTSADMIN)
admin.site.register(INC_REPORTED_METHOD)
admin.site.register(INC_TYPE)
admin.site.register(INC_IMPACT)
admin.site.register(INC_SEVERITY)
admin.site.register(INC_RESPONSE)
admin.site.register(INC_ROOT_CAUSE)
admin.site.register(INC_REMEDIAL,INC_REMEDIALADMIN)


