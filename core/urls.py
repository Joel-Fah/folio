from django.urls import path
from .views import HomeView, ProjectDetailView, WorksView, AboutView, ConnectView, MessageView, MessageDetailView

# Create your urls here.

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', WorksView.as_view(), name='projects'),
    path('projects/<int:id>/<slug:slug>/', ProjectDetailView.as_view(), name='details'),
    path('about/', AboutView.as_view(), name='about'),
    path('connect/', ConnectView.as_view(), name='connect'),
    path('messages/', MessageView.as_view(), name='messages'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_details'),
]
