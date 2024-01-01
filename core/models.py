from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 150, blank=False, null=False)
    content = QuillField()
    client = models.CharField(max_length = 150)
    role = models.CharField(max_length = 150)
    link = models.URLField(max_length = 200)
    
    started_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    ended_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length = 150, blank=False, null=False)
    
    def __str__(self):
        return self.name