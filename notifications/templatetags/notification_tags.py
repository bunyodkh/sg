from django import template
from ..models import CTAMessage, SiteNotification

register = template.Library()

@register.simple_tag
def get_active_cta():
    return CTAMessage.objects.filter(show=True).order_by('-created_at').first()


@register.simple_tag
def get_notification():
    return SiteNotification.objects.filter(show=True).order_by('-created_at').first()