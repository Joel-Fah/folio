import random
from typing import Any
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from .models import Project, Tag, AcademicAchievement, Certification, Volunteering

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
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tool"] = random.choice(['angle-tool', 'hammer', 'tools', 'ruler-combine', 'color-filter', 'color-picker', 'frame-alt-empty', 'crop', 'component'])
        context["emoji"] = random.choice(['emoji-satisfied', 'emoji-surprise-alt', 'emoji-surprise', 'emoji-blink-left', 'emoji-blink-right'])
        context['academics'] = AcademicAchievement.objects.all()
        context['certifications'] = Certification.objects.all()
        context['volunteerings'] = Volunteering.objects.all()
        return context
    
    
# Custom error pages (404, 500)

def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_error_view(request):
    return render(request, 'errors/500.html', status=500)