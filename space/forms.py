from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'name', 'email', 'phone', 'region', 'startup_name', 'startup_description', 'startup_pitchdeck',
            'startup_stage', 'problem', 'solution', 'traction', 'team_description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your fullname')}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your email address to which we can reply')}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your phone to which we can call')}),
            'region': forms.Select(attrs={'class': 'form-input'}),
            'startup_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Your startup name')}),
            'startup_description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': _('Describe your startup'), 'rows': 3}),
            'startup_pitchdeck': forms.TextInput(attrs={'class': 'form-input', 'placeholder': _('Link to your pitchdeck')}),
            'startup_stage': forms.Select(attrs={'class': 'form-input'}),
            'problem': forms.Textarea(attrs={'class': 'form-input', 'placeholder': _('What and whose problem are you solving?'), 'rows': 2}),
            'solution': forms.Textarea(attrs={'class': 'form-input', 'placeholder': _('Describe your solution'), 'rows': 2}),
            'traction': forms.Textarea(attrs={'class': 'form-input', 'placeholder': _('Describe your traction'), 'rows': 2}),
            'team_description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': _('Describe your team'), 'rows': 2}),
        }
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'phone': _('Phone'),
            'region': _('Region'),
            'startup_name': _('Startup Name'),
            'startup_description': _('Startup Description'),
            'startup_pitchdeck': _('Startup Pitchdeck'),
            'startup_stage': _('Startup Stage'),
            'problem': _('Problem'),
            'solution': _('Solution'),
            'traction': _('Traction'),
            'team_description': _('Team Description'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

        select_fields = {
            'region': _('Select your region'),
            'startup_stage': _('Select startup stage'),
        }
        for field, empty_label in select_fields.items():
            if field in self.fields:
                choices = list(self.fields[field].choices)
                if choices and choices[0][0] == '':
                    choices[0] = ('', empty_label)
                else:
                    choices = [('', empty_label)] + choices
                self.fields[field].choices = choices
    
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
    
    def clean_startup_name(self):
        value = self.cleaned_data.get('startup_name')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Startup name is required."))
        return str(value).strip()

    def clean_startup_description(self):
        value = self.cleaned_data.get('startup_description')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Startup description is required."))
        return str(value).strip()

    def clean_startup_stage(self):
        value = self.cleaned_data.get('startup_stage')
        if not value:
            raise forms.ValidationError(_("Startup stage is required."))
        return value

    def clean_problem(self):
        value = self.cleaned_data.get('problem')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Problem is required."))
        return str(value).strip()

    def clean_solution(self):
        value = self.cleaned_data.get('solution')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Solution is required."))
        return str(value).strip()

    def clean_traction(self):
        value = self.cleaned_data.get('traction')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Traction is required."))
        return str(value).strip()

    def clean_team_description(self):
        value = self.cleaned_data.get('team_description')
        if not value or not str(value).strip():
            raise forms.ValidationError(_("Team description is required."))
        return str(value).strip()
    
    def clean_startup_pitchdeck(self):
        email = self.cleaned_data.get('startup_pitchdeck')
        if not email or not str(email).strip():
            raise forms.ValidationError(_("Pitchdeck is required."))
        return str(email).strip()