from django.urls import path
from .views import HomeView, ProjectDetailView

# Create your urls here.

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project/<int:id>/<slug:slug>/', ProjectDetailView.as_view(), name='details'),
]
