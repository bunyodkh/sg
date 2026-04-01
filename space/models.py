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
    startup_description = models.TextField(help_text=_('Startup Description'), blank=True, null=True)
    startup_pitchdeck = models.CharField(max_length=100, help_text=_('Startup Pitchdeck'), blank=True, null=True)

    STARTUP_STAGE_CHOICES = [
        ('idea_prototype', _('Idea/Prototype')),
        ('mvp', _('MVP')),
        ('first_users', _('First Users')),
        ('revenue', _('Revenue')),
        ('breakeven_point', _('Breakeven Point')),
    ]

    startup_stage = models.CharField(
        max_length=20,
        choices=STARTUP_STAGE_CHOICES,
        verbose_name=_('Startup Stage'),
        blank=True,
        null=True,
        help_text=_('Current stage of the startup'),
    )

    problem = models.TextField(
        help_text=_('For whom and what is the problem?'),
        blank=True,
        null=True,
    )

    team_description = models.TextField(
        help_text=_('Describe your team'),
        blank=True,
        null=True,
    )

    solution = models.TextField(
        help_text=_('Describe the solution your startup offers'),
        blank=True,
        null=True,
    )

    traction = models.TextField(
        help_text=_('Briefly describe the traction your startup has achieved'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Participant")
        verbose_name_plural = _("Participants")
        ordering = ['-id']

