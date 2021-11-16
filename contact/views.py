from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages,auth
from django.contrib.auth.models import User

# Create your views here.
def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['gmarshal070@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contact/contact.html", {'form': form})

def thanks(request):
    return render(request, 'contact/contact_form_sent.html')
