from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your fullname')}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': _('Your email address to which we can reply')}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': _('Describe how would you like to contribute')}),
        }
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'message': _('Message'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not str(name).strip():
            raise forms.ValidationError(_("Name is required."))
        return str(name).strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not str(email).strip():
            raise forms.ValidationError(_("Email is required."))
        return str(email).strip()

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message or not str(message).strip():
            raise forms.ValidationError(_("Message is required."))
        return str(message).strip()