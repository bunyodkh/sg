from django.urls import path

from .views import (
    index, 

    explore_startups,
    startup_category_detail,
    startup_development_stage_detail,
    startup_funding_stage_detail,

    explore_organizations,
    organization_type_detail,
    
    explore_programs,
    startup_support_program_detail,

    show_404
)

app_name = 'registry'

urlpatterns = [
    path('', index, name='index'),
    
    path('explore/startups', explore_startups, name='explore-startups'),
    path('explore/startups/spheres/<slug:slug>', startup_category_detail, name='startup-category-detail'),
    path('explore/startups/dev-stages/<slug:slug>', startup_development_stage_detail, name='startup-development-stage-detail'),
    path('explore/startups/funding-stages/<slug:slug>', startup_funding_stage_detail, name='startup-funding-stage-detail'),
    
    path('explore/organizations', explore_organizations, name='explore-organizations'),
    path('explore/organizations/<slug:slug>/', organization_type_detail, name='organization-type-detail'),
    
    path('explore/programs', explore_programs, name='explore-programs'),
    path('explore/programs/type/<slug:slug>/', startup_support_program_detail, name='startup-support-program-detail'),

    path('404', show_404, name='not-found')
]