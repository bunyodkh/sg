from django.urls import path

from .views import (
    index, 
    explore_startups,
    explore_organizations,
    explore_programs,
    show_404
)

app_name = 'registry'

urlpatterns = [
    path('', index, name='index'),
    path('explore/startups', explore_startups, name='explore-startups'),
    path('explore/organizations', explore_organizations, name='explore-organizations'),
    path('explore/programs', explore_programs, name='explore-programs'),
    path('404', show_404, name='not-found')
]