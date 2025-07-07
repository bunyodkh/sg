from django.shortcuts import render

from .models import Startup, Organization, SupportProgram


def index(request):
    return render(request, 'index.html', {})


def explore_startups(request):
    startups = Startup.objects.all().order_by('name')
    return render(request, 'explore_startups.html', { 'startups': startups })


def explore_organizations(request):
    organizations = Organization.objects.all().order_by('name')
    return render(request, 'explore_organizations.html', { 'organizations': organizations })


def explore_programs(request):
    programs = SupportProgram.objects.all().order_by('name')
    return render(request, 'explore_programs.html', { 'programs': programs })


def show_404(request):
    return render(request, '404.html', {})