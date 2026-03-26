from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(ModelAdmin):
    list_display = ['name', 'email', 'phone', 'region', 'startup_name', 'created_at']
    search_fields = ['name', 'email', 'phone', 'region', 'startup_name']
