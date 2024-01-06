from django.contrib.sitemaps import Sitemap
from .models import Project

class ProjectSitemap(Sitemap):
    changefreq = "weekly"  # Set the change frequency
    priority = 0.8  # Set the priority (0.0 to 1.0)

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # Set the last modification date field of your model