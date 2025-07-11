from django.contrib import admin
from unfold.admin import ModelAdmin
from django import forms


from .models import (
    Startup, 
    StartupCategory, 
    TargetAudience,

    Organization, 
    OrganizationType,
    OrganizationAffiliation,
    Investment, 
    InvestmentStage,
    DevelopmentStage,

    SupportProgram,
    SupportProgramType,
    SupportProgramCycle,
)


@admin.register(Startup)
class StartupAdmin(ModelAdmin):
    list_display = ('name', 'website', 'operation_status')
    search_fields = ('name', 'description', 'website')
    list_filter = ('categories',)
    filter_horizontal = ('categories',)



@admin.register(StartupCategory)
class StartupCategoryAdmin(ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)

    
@admin.register(InvestmentStage)
class InvestmentStageAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(DevelopmentStage)
class DevelopmentStageAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Organization)
class OrganizationAdmin(ModelAdmin):
    list_display = ('name', 'organization_type', 'affiliation',)
    search_fields = ('name', 'description', 'website', 'email')
    list_filter = ('organization_type',)

    

@admin.register(Investment)
class InvestmentAdmin(ModelAdmin):
    list_display = ('investor', 'startup', 'amount', 'created_at')
    search_fields = ('investor__name', 'startup__name')
    list_filter = ('investor', 'startup')



@admin.register(TargetAudience)
class TargetAudienceAdmin(ModelAdmin):
    list_display = ('audience', 'created_at')
    search_fields = ('audience',)
    list_filter = ('created_at',)


@admin.register(OrganizationType)
class OrganizationType(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(OrganizationAffiliation)
class OrganizationAffiliationAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(SupportProgram)
class SupportProgramAdmin(ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description', 'website')
    list_filter = ('cycles',)
    filter_vertical = ('managing_organizations',)


@admin.register(SupportProgramType)
class SupportProgramTypeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(SupportProgramCycle)
class SupportProgramCycleAdmin(ModelAdmin): 
    list_display = ('name', 'program','status', 'start_date', 'end_date')
    search_fields = ('name', 'program')
    list_filter = ('status', 'start_date', 'end_date')
