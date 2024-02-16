from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import format_html
from django.db import models
from .models import Project, Tag, AcademicAchievement, Certification, Volunteering, Message
from django_summernote.admin import SummernoteModelAdmin

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
    
class ProjectAdmin(SummernoteModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    list_display = ['id', 'name', 'is_visible', 'link']
    
    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }
    
    summernote_fields = ('content')
    
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['id', 'name', 'get_project_name']
    search_fields = ['name']
    list_filter = ['name']
    
    @admin.display(description='Project name', ordering='project__name')
    def get_project_name(self, obj):
        return obj.project.name
    
class AcademicAchievementAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'institution', 'is_visible']
    search_fields = ['title', 'institution']
    list_filter = ['title', 'institution']
    
    summernote_fields = ('description')

class CertificationAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'organisation', 'is_visible']
    search_fields = ['title', 'organisation']
    list_filter = ['title', 'organisation']
    
    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }
    
    summernote_fields = ('description')

class VolunteeringAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'organisation', 'is_visible']
    search_fields = ['title', 'organisation']
    list_filter = ['title', 'organisation']
    
    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminFileWidget}
    }
    
    summernote_fields = ('description')
    
class MessageAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name', 'is_visible']
    search_fields = ['name', 'message']
    list_filter = ['name']
    
    summernote_fields = ('message')

# Register in admin dashboard
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(AcademicAchievement, AcademicAchievementAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Volunteering, VolunteeringAdmin)
admin.site.register(Message, MessageAdmin)