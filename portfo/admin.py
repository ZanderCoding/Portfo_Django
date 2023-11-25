from django.contrib import admin

from .models import Skill, Contact, Project

# Register your models here.
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Project)
