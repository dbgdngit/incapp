from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
    
class INC_REPORTED_METHOD(models.Model):
    methodlabel = models.CharField(max_length=12,default='')

    def __unicode__(self):
        return unicode(self.methodlabel)

class INC_TYPE(models.Model):
    inctypelabel = models.CharField(max_length=30,default='')

    def __unicode__(self):
        return unicode(self.inctypelabel)

class INC_IMPACT(models.Model):
    impactlabel = models.CharField(max_length=20,default='')

    def __unicode__(self):
        return unicode(self.impactlabel)

class INC_SEVERITY(models.Model):
    description = models.CharField(max_length=50)
    value = models.IntegerField(default='1')

    def __unicode__(self):
        return self.description

class INC_RESPONSE(models.Model):
    response_description = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.response_description)

class INC_ROOT_CAUSE(models.Model):
    root_description = models.CharField(max_length=30)

    def __unicode__(self):
        return unicode(self.root_description) 

class INCIDENT(models.Model):
    incref = models.CharField(max_length=9)
    date_reported = models.DateTimeField('reported on')
    date_happened = models.DateTimeField('happened on')
    reported_by = models.CharField(max_length=100)
    reported_method = models.ForeignKey("INC_REPORTED_METHOD", on_delete=models.CASCADE)
    incident_summary_headline = models.CharField(max_length=100)
    incident_type = models.ForeignKey("INC_TYPE", on_delete=models.CASCADE)
    incident_impact = models.ManyToManyField("INC_IMPACT")
    incident_severity = models.ForeignKey("INC_SEVERITY", on_delete=models.CASCADE)
    incident_response_actions = models.ManyToManyField("INC_RESPONSE")
    incident_recovery_time = models.IntegerField(null=True)
    incident_detail = models.TextField
    incident_remedial_actions = models.ManyToManyField("INC_REMEDIAL")
    linked_risk_ref = models.CharField(max_length=30)
    incident_root_cause = models.ForeignKey("INC_ROOT_CAUSE", on_delete=models.CASCADE)

def __unicode__(self):
        return unicode(self.incident_summary_headline)

class INC_REMEDIAL(models.Model):
    description = models.CharField(max_length=50)
    action_owner = models.CharField(max_length=30)
    status = models.CharField(max_length=12)
    date_raised = models.DateTimeField('date raised')

    def __unicode__(self):
        return self.description 
    
class INCIDENTSADMIN(admin.ModelAdmin):     
    ordering = ('date_reported','incref')
    list_display = ('date_reported','incref','incident_summary_headline','incident_severity')

class INC_REMEDIALADMIN(admin.ModelAdmin):
    ordering = ('date_raised','status')
    list_display = ('date_raised','status','description','action_owner')







