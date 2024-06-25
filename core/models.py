from django.db import models
from slugify import slugify

# Create your models here.

class Project(models.Model):
    
    class Filters(models.TextChoices):
        DESIGN = 'design', 'ui.ux design'
        GRAPHICS = 'graphics', 'graphics'
        DEVELOPMENT = 'development', 'development'
    
    name = models.CharField(max_length = 150, blank=False, null=False)
    # content = tinymce_models.HTMLField(blank=True, null=True)
    content = models.TextField(blank=True, null=True, help_text='Add <b>class="project"</b> to your <ul> elements if any')
    client = models.CharField(max_length = 150, blank=True, null=True, help_text='Leave blank if none')
    role = models.CharField(max_length = 150, blank=True, null=True, help_text='Leave blank if none')
    link = models.URLField(max_length = 200, blank=True, null=True, help_text='Leave blank if none')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    category = models.CharField(max_length=255, choices=Filters.choices, default=Filters.DESIGN)
    
    started_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    ended_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    slug = models.SlugField(max_length = 200, default="", editable=False)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Auto populate slug field from project name field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects', blank=True, null=True)
    name = models.CharField(max_length = 150, blank=False, null=False)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
# About Page models
class AcademicAchievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_earned = models.DateField()
    institution = models.CharField(max_length=255)
    image = models.ImageField(upload_to='achievements/academics/', blank=True, null=True)
    link = models.URLField(max_length = 200, blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_earned = models.DateField()
    organisation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='achievements/certifications/', blank=True, null=True)
    link = models.URLField(max_length = 255, blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

class Volunteering(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    organisation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='achievements/volunteering/', blank=True, null=True)
    link = models.URLField(max_length = 255, blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
class Message(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default="Anonymous")
    message = models.TextField(blank=True, null=True)
    social = models.URLField(max_length=255, blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
