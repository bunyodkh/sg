from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone', 'region', 'startup_name', 'startup_pitchdeck']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your fullname')}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your email address to which we can reply')}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your phone to which we can call')}),

            'region': forms.Select(attrs={'class': 'form-input'}),

            'startup_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your startup name')}),
            'startup_pitchdeck': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Link to your pitchdeck')}),
        }
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'phone': _('Phone'),
            'region': _('Region'),
            'startup_name': _('Startup Name'),
            'startup_pitchdeck': _('Startup Pitchdeck'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        if 'region' in self.fields:
            choices = list(self.fields['region'].choices)            
            choices[0] = ('', _("Select your region"))
            self.fields['region'].choices = choices
    
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

    def clean_phone(self):
        email = self.cleaned_data.get('phone')
        if not email or not str(email).strip():
            raise forms.ValidationError(_("Phone is required."))
        return str(email).strip()
    
    def clean_region(self):
        region = self.cleaned_data.get('region')
        if not region:
            raise forms.ValidationError(_("Region is required."))
        return region
    
    def clean_stratup_name(self):
        email = self.cleaned_data.get('stratup_name')
        if not email or not str(email).strip():
            raise forms.ValidationError(_("Startup name is required."))
        return str(email).strip()
    
    def clean_startup_pitchdeck(self):
        email = self.cleaned_data.get('startup_pitchdeck')
        if not email or not str(email).strip():
            raise forms.ValidationError(_("Pitchdeck is required."))
        return str(email).strip()