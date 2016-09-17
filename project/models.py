# -*- coding:gbk -*-
from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    state = models.CharField(max_length=20,default='1')
    
class Plan(models.Model):
    project = models.ForeignKey(Project,null=True)
    create_time = models.DateTimeField(null=True)
    json_data = models.TextField(default='')
    version = models.CharField(max_length=40,null=True)

class Task(models.Model):
    plan = models.ForeignKey(Plan,null=True)
    code = models.CharField(max_length=20,null=True)
    parent = models.ForeignKey('Task',null=True)
    name = models.CharField(max_length=200,null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    duration = models.IntegerField(null=True)
    resource = models.CharField(max_length=200,null=True)
