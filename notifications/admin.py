from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import SiteNotification, CTAMessage


@admin.register(SiteNotification)
class SiteNotificationAdmin(ModelAdmin):
    list_display = ('show', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'message')
    ordering = ('-created_at',)


@admin.register(CTAMessage)
class CTAMessageAdmin(ModelAdmin):  
    list_display = ('show', 'message', 'link_text', 'created_at')
    search_fields = ('message', 'link_text')
    ordering = ('-created_at',)
    list_filter = ('created_at',)
