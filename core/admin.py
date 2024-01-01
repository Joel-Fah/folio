from django.contrib import admin
from .models import Project, Tag

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    
class TagAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)