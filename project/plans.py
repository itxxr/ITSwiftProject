# *+* coding: utf8 *+*
from django.shortcuts import render
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from .models import Plan
from .models import Project
from datetime import datetime

def showProjectPlan(request,project_id):
    project = Project.objects.get(pk=project_id)
    plan_id = project.plan_set.order_by('-create_time')[0].id
    return render(request,"project/OnePlan.html",{'plan_id':plan_id})
    
def showPlan(request,plan_id):
    return render(request,"project/OnePlan.html",{'plan_id':plan_id})

def loadPlanData(request,plan_id):
    resources = []
    allUsers = User.objects.all()
    for u in allUsers :
        resources.append({'id':u.id,'name':u.first_name +' '+u.last_name})
    roles = [{'id':'1','name':'员工'}]
    tasks = json.loads(Plan.objects.get(pk=plan_id).json_data)
    data = tasks
    data['resources']=resources
    data['roles']=roles
    return JsonResponse(data)

def savePlanData(request):
    plan = Plan.objects.get(pk=request.POST['id'])
    plan_id=plan.project.plan_set.order_by('-create_time')[0].id
    if str(plan_id) != request.POST['id'] :
        return JsonResponse({'errMsg':'The plan is not newest,please refresh.newest plan ID:'+str(plan_id)+' current plan ID:'+request.POST['id']})
    plan.json_data=request.POST['json_data']
    plan.id=None
    plan.create_time = datetime.now()
    plan.save()
    return JsonResponse({})

    