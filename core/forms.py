from django import forms
from django.forms.widgets import TextInput, URLInput, Textarea
from .models import Message

#  Create your forms here

class MessageForm(forms.ModelForm):
    
    class Meta:
        model = Message
        fields = ['name', 'social', 'message']
        
        widgets = {
            'name': TextInput(
                attrs={
                    'name': 'name',
                    'id': 'name',
                    'placeholder': 'Anonymous',
                    'class': 'border border-hoverColor/50 rounded-lg bg-hoverColor/20 my-1 placeholder:text-yellowWhite/50 focus:ring-1'
                }
            ),
            
            'social': URLInput(
                attrs={
                    'name': 'social',
                    'id': 'social',
                    'placeholder': 'https://x.com/FahDejon',
                    'class': 'border border-hoverColor/50 rounded-lg bg-hoverColor/20 my-1 placeholder:text-yellowWhite/50 focus:ring-1'
                }
            ),
            
            'message': Textarea(
                attrs={
                    'name': 'message',
                    'id': 'message',
                    'placeholder': 'Write your message here...',
                    'maxlength': 300,
                    'class': 'border border-hoverColor/50 rounded-lg bg-hoverColor/20 my-1 resize-none h-40 placeholder:text-yellowWhite/50 focus:ring-1'
                }
            ),
        }
        