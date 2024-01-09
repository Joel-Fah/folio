from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models
from .models import Project, Tag

# Register your models here.

class CustomAdminFileWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if hasattr(value, "url"):
            result.append(
                f'''<a href="{value.url}" target="_blank">
                      <img 
                        src="{value.url}" alt="{value}" 
                        width="150" height="150"
                        style="object-fit: contain;"
                      />
                    </a>'''
            )
        result.append(super().render(name, value, attrs, renderer))
        return format_html("".join(result))
    
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    list_display = ['id', 'name', 'is_visible', 'link']
    
    formfield_overrides = {           # Here
        models.ImageField: {"widget": CustomAdminFileWidget}
    }
    
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_filter = ['name']
    search_fields = ['name']
    list_display = ['id', 'name', 'get_project_name']
    
    @admin.display(description='Project name', ordering='project__name')
    def get_project_name(self, obj):
        return obj.project.name
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)