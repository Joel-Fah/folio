from django.urls import path
from .views import HomeView, ProjectDetailView, AboutView

# Create your urls here.

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project/<int:id>/<slug:slug>/', ProjectDetailView.as_view(), name='details'),
    path('about/', AboutView.as_view(), name='about'),
]
