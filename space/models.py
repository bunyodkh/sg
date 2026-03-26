from django.db import models
from django.utils.translation import gettext_lazy as _


class Participant(models.Model):
    name = models.CharField(max_length=100, help_text=_('Name'), blank=True, null=True)
    email = models.CharField(max_length=100, help_text=_('Email'), blank=True, null=True)
    phone = models.CharField(max_length=100, help_text=_('Phone'), blank=True, null=True)

    REGION_CHOICES = [
        ('andijan', _('Andijan')),
        ('ferghana', _('Ferghana')),
        ('namangan', _('Namangan')),
        ('surkhandarya', _('Surkhandarya')),
    ]

    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name=_('Region'), blank=True, null=True)

    startup_name = models.CharField(max_length=100, help_text=_('Startup Name'), blank=True, null=True)
    startup_pitchdeck = models.CharField(max_length=100, help_text=_('Startup Pitchdeck'), blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Participant")
        verbose_name_plural = _("Participants")
        ordering = ['-id']

