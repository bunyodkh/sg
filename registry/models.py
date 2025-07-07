from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class Startup(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=False, null=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    website = models.CharField(_("Website"), blank=True, null=True)
    categories = models.ManyToManyField('StartupCategory', verbose_name=_("Categories"), blank=True, related_name='startups')
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    country = CountryField(_("Country"), blank_label=_("Select Country"), blank=True, null=True)
    region = models.CharField(_("Region"), max_length=100, blank=True, null=True)

    target_audience = models.ManyToManyField('TargetAudience', verbose_name=_("Target Audience"), blank=True, related_name='startups', help_text=_("Target audience for the startup"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Startup")
        verbose_name_plural = _("Startups")
        ordering = ['name']



class StartupCategory(models.Model):
    category = models.CharField(_("Category"), max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = _("Startup Category")
        verbose_name_plural = _("Startup Categories")
        ordering = ['category']



class TargetAudience(models.Model): 
    audience = models.CharField(_("Audience"), max_length=100, blank=False, null=False, help_text=_("Target audience for the startup"))

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.audience}"

    class Meta:
        verbose_name = _("Target Audience")
        verbose_name_plural = _("Target Audiences")
        ordering = ['audience']



class Organization(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=False, null=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    website = models.CharField(_("Website"), blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    capacity = models.DecimalField(_("Funds Available"), max_digits=15, decimal_places=0, blank=True, null=True, help_text=_("Total funds available for investment in USD"))

    organization_type = models.CharField(_("Organization Type"), max_length=50, choices=[
        ('investor', _("Investor")),
        ('support_organization', _("Support Organization")),
    ], default='investor', help_text=_("Organization Type"))

    investor_type = models.ForeignKey('InvestorType', verbose_name=_("Type"), on_delete=models.SET_NULL, blank=True, null=True, related_name='investors')
    affiliation = models.ForeignKey('OrganizationAffiliation', verbose_name=_("Affiliation"), on_delete=models.SET_NULL, blank=True, null=True, related_name='investors')
    apply_link = models.CharField(_("Application Link"), blank=True, null=True, help_text=_("Link to apply for investment or partnership"))

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ['name']



class InvestorType(models.Model):
    name = models.CharField(_("Type Name"), max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization Type")
        verbose_name_plural = _("Organization Types")
        ordering = ['name']


class OrganizationAffiliation(models.Model):
    name = models.CharField(_("Type Name"), max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization Affiliation")
        verbose_name_plural = _("Organization Affiliations")
        ordering = ['name']


class Investment(models.Model):
    startup = models.ForeignKey('Startup', verbose_name=_("Startup"), on_delete=models.CASCADE, related_name='investments')
    investor = models.ForeignKey('Organization', verbose_name=_("Investor"), on_delete=models.CASCADE, related_name='investments')
    amount = models.DecimalField(_("Investment Amount"), max_digits=15, decimal_places=0, blank=False, null=False)
    details = models.TextField(_("Details"), blank=True, null=True, help_text=_("Additional details about the investment"))
    date = models.DateField(_("Investment Date"), blank=True, null=True, help_text=_("Date of the deal"))
    stage = models.ForeignKey('InvestmentStage', verbose_name=_("Investment Stage"), on_delete=models.SET_NULL, blank=True, null=True, related_name='investments')    

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.investor.name} invested in {self.startup.name}"

    class Meta:
        verbose_name = _("Investment")
        verbose_name_plural = _("Investments")
        ordering = ['date']



class InvestmentStage(models.Model):
    name = models.CharField(_("Stage Name"), max_length=50, blank=False, null=False)
    description = models.TextField(_("Description"), max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Startup Stage")
        verbose_name_plural = _("Startup Stage")
        ordering = ['created_at']

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)



class SupportProgram(models.Model):
    name = models.CharField(_("Name"), max_length=255, blank=False, null=False)
    description = models.TextField(_("Description"), blank=True, null=True)
    website = models.CharField(_("Website"), blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)

    managing_organizations = models.ManyToManyField('Organization', verbose_name=_("Managing Organizations"), blank=True, related_name='programs', help_text=_("Organizations managing the incubator program"))

    mode = models.CharField(_("Mode"), max_length=50, choices=[
        ('online', _("Online")),
        ('offline', _("Offline")),
        ('hybrid', _("Hybrid"))
    ], default='online', help_text=_("Mode of operation for the incubator"))

    country = CountryField(_("Country"), blank_label=_("Select Country"), blank=True, null=True)
    region = models.CharField(_("Region"), max_length=100, blank=True, null=True)

    program_type = models.ForeignKey('SupportProgramType', verbose_name=_("Program Type"), on_delete=models.SET_NULL, blank=True, null=True, related_name='programs', help_text=_("Type of support program"))
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    status = models.CharField(_("Status"), max_length=50, choices=[
        ('active', _("Active")),
        ('inactive', _("Inactive")),
        ('archived', _("Archived"))
    ], default='active', help_text=_("Current status of the incubator program"))

    def __str__(self):
        return self.name
    
    def get_active_cycle(self):
        """
        Returns the first upcoming or ongoing cycle for this support program, or None if none exist.
        """
        return self.cycles.filter(status__in=['upcoming', 'ongoing']).order_by('start_date').first()

    class Meta:
        verbose_name = _("Support Program")
        verbose_name_plural = _("Support Programs")
        ordering = ['name']


class SupportProgramType(models.Model): 
    name = models.CharField(_("Type"), max_length=100, blank=False, null=False)
    description = models.TextField(_("Description"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Support Program Type")
        verbose_name_plural = _("Support Program Types")
        ordering = ['name']


class SupportProgramCycle(models.Model):
    program = models.ForeignKey('SupportProgram', verbose_name=_("Program"), on_delete=models.CASCADE, related_name='cycles')
    name = models.CharField(_("Cycle Name"), max_length=100, blank=False, null=False)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    
    status = models.CharField(_("Status"), max_length=50, choices=[
        ('upcoming', _("Upcoming")),
        ('ongoing', _("Ongoing")),
        ('completed', _("Completed")),
        ('cancelled', _("Cancelled"))
    ], default='upcoming', help_text=_("Current status of the program cycle"))
    
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    
    duration = models.CharField(_("Duration"), max_length=100, blank=True, null=True, help_text=_("Duration of the program (e.g., 6 months, 1 year)"))
    capacity = models.CharField(_("Capacity"), blank=True, null=True, help_text=_("Maximum number of startups that can be supported at a time"))

    notes = models.TextField(_("Notes"), blank=True, null=True, help_text=_("Additional notes about the program cycle"))
    participating_startups = models.ManyToManyField('Startup', verbose_name=_("Participating Startups"), blank=True, related_name='program_cycles', help_text=_("Startups participating in this program cycle"))

    fee_structure = models.TextField(_("Fee Structure"), blank=True, null=True, help_text=_("Details about the fee structure for the program (if any)"))
    
    application_status = models.CharField(_("Application Status"), max_length=50, choices=[
        ('open', _("Open")),
        ('closed', _("Closed")),
        ('will be announced', _("Will be announced")),
    ], default='open', help_text=_("Current application status for the program cycle"))
    
    apply_link = models.CharField(_("Application Link"), blank=True, null=True, help_text=_("Link to apply for the incubator program"))


    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"{self.program.name} - {self.name}"

    class Meta:
        verbose_name = _("Support Program Cycle")
        verbose_name_plural = _("Support Program Cycles")
        ordering = ['start_date']