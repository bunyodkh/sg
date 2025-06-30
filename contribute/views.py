from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import MessageForm

def contribute(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you for your message. We will contact you very soon."))
            form = MessageForm()  # Reset form after success
        else:
            messages.error(request, _("Please correct the errors below."))
    else:
        form = MessageForm()

    return render(request, 'contribute.html', { 'form': form })