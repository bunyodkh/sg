from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Message


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    


