from typing import Any
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from .models import Project, Tag

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    
class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project
    
    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['id'], slug=self.kwargs['slug'])