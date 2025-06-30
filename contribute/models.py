from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'), blank=False, null=False)
    email = models.CharField(max_length=100, help_text=_('Email'), blank=True, null=True)
    message = models.TextField(max_length=1000, help_text=_('Message'), blank=False, null=False)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ['-id']