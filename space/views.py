from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import ParticipantForm


def main_space(request):
    return render(request, 'index.html')


def startup_support_program(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you for your application. We will contact you very soon."))
            form = ParticipantForm()  # Reset form after success
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = ParticipantForm()

    return render(request, 'startup_support_program.html', { 'form': form })
