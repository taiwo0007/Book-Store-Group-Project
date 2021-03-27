from django.shortcuts import render
from .models import Contact
from django.views.generic import View
from .forms import ContactForm
from django.contrib import messages


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(request, "contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            contact = Contact()
            contact.firstname = firstname
            contact.lastname = lastname
            contact.email = email
            contact.subject = subject
            contact.save()
            messages.info(self.request, "Your message has been received.")
            return render(request,'thanks_contact.html')
