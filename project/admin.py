from django.contrib import admin

from .models import Project
from .models import Plan

admin.site.register(Project)
admin.site.register(Plan)
