from django.conf.urls import patterns, include, url

from . import plans

urlpatterns = [
    url(r'^showProjectPlan/(?P<project_id>[0-9]+)$', plans.showProjectPlan, name='showProjectPlan'),
    url(r'^showPlan/(?P<plan_id>[0-9]+)$', plans.showPlan, name='showPlan'),
    url(r'^loadPlanData/(?P<plan_id>[0-9]+)$',plans.loadPlanData,name='loadPlanData'),
    url(r'^savePlanData',plans.savePlanData,name='savePlanData')    
]
