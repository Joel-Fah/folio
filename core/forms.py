from django import forms
from django.forms.widgets import TextInput, URLInput, Textarea
from .models import Message
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.conf import settings
from django.urls import reverse
from django.templatetags.static import static


#  Create your forms here

# Custom Summernote WYSIWIG specific to this form
# class SummernoteModelAdminWithCustomToolbar(SummernoteWidget):
#     def summernote_settings(self):
#         summernote_settings = settings.SUMMERNOTE_CONFIG.get('summernote', {}).copy()
#         lang = settings.SUMMERNOTE_CONFIG['summernote'].get('lang')
#         if not lang:
#             lang = 'en-US'
#         summernote_settings.update({
#             'lang': lang,
#             'url': {
#                 'language': static('summernote/lang/summernote-' + lang + '.min.js'),
#                 'upload_attachment': reverse('django_summernote-upload_attachment'),
#                 },
#             'width': '100%',
#             'height': '200px',
#             'toolbar': [
#                 ['font', ['bold', 'italic', 'underline', ]],
#                 ['misc', ['link', 'undo', 'redo', ]],
#             ],
#             'js': ()
#         })
#         return summernote_settings

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
                    'class': 'rounded-lg text-darkBlue bg-white placeholder:text-darkBlue/50 focus:ring-1',
                }
            ),
            
            'social': URLInput(
                attrs={
                    'name': 'social',
                    'id': 'social',
                    'placeholder': 'https://x.com/@username',
                    'class': 'rounded-lg text-darkBlue bg-white placeholder:text-darkBlue/50 focus:ring-1',
                }
            ),
            
            'message': Textarea(
                attrs={
                    'name': 'message',
                    'id': 'message',
                    'placeholder': 'Write your message here...',
                    'maxlength': 300,
                    'cols': '',
                    'rows': '',
                    'style': 'height: 12rem; resize: none;',
                    'class': 'rounded-lg text-darkBlue bg-white placeholder:text-darkBlue/50 focus:ring-1',
                }
            ),
        }
        