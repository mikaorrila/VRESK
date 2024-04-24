from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    pass


# Register your models with ModelAdmin classes

admin.site.register(Project, ProjectAdmin)