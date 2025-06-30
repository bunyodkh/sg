from django.shortcuts import render

from .models import Startup, Investor, SupportProgram


def index(request):
    return render(request, 'index.html', {})


def explore_startups(request):
    startups = Startup.objects.all().order_by('name')
    return render(request, 'explore_startups.html', { 'startups': startups })


def explore_investors(request):
    investors = Investor.objects.all().order_by('name')
    return render(request, 'explore_investors.html', { 'investors': investors })


def explore_programs(request):
    programs = SupportProgram.objects.all().order_by('name')
    return render(request, 'explore_programs.html', { 'programs': programs })


def show_404(request):
    return render(request, '404.html', {})