from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import (
    Startup, 
    Organization, 
    SupportProgram, 
    OrganizationType,
    StartupCategory,
    DevelopmentStage,
    InvestmentStage,
    SupportProgramType
)


def index(request):
    return render(request, 'index.html', {})


def explore_startups(request):
    startup_list = Startup.objects.all().order_by('name')
    paginator = Paginator(startup_list, 12)
    page_number = request.GET.get('page')
    startups = paginator.get_page(page_number)
    return render(request, 'explore_startups.html', { 'startups': startups })


def startup_category_detail(request, slug):
    category = get_object_or_404(StartupCategory, slug=slug)
    startups = category.startups.all()
    return render(request, 'explore_startups.html', {
        'category': category,
        'startups': startups,
    })


def startup_development_stage_detail(request, slug):
    stage = get_object_or_404(DevelopmentStage, slug=slug)
    startups = stage.startups.all()
    return render(request, 'explore_startups.html', {
        'stage': stage,
        'startups': startups,
    })


def startup_funding_stage_detail(request, slug):
    stage = get_object_or_404(InvestmentStage, slug=slug)
    startups = stage.startups.all()
    return render(request, 'explore_startups.html', {
        'stage': stage,
        'startups': startups,
    })


def explore_organizations(request):
    organization_list = Organization.objects.all().order_by('name')
    paginator = Paginator(organization_list, 10)  
    page_number = request.GET.get('page')
    organizations = paginator.get_page(page_number)
    return render(request, 'explore_organizations.html', { 'organizations': organizations })


def organization_type_detail(request, slug):
    org_type = OrganizationType.objects.get(slug=slug)
    organizations = org_type.organizations.all()
    return render(request, 'explore_organizations.html', {
        'organization_type': org_type,
        'organizations': organizations,
    })


def explore_programs(request):
    program_list = SupportProgram.objects.all().order_by('name')
    paginator = Paginator(program_list, 10) 
    page_number = request.GET.get('page')
    programs = paginator.get_page(page_number)
    return render(request, 'explore_programs.html', { 'programs': programs })


def startup_support_program_detail(request, slug):
    program_type = get_object_or_404(SupportProgramType, slug=slug)
    programs = SupportProgram.objects.filter(program_type=program_type)
    return render(request, 'explore_programs.html', {
        'program_type': program_type,
        'programs': programs,
    })


def show_404(request):
    return render(request, '404.html', {})