from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def contactView(request):
    if request.method=="POST":
        contact=Contact()
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.firstname=firstname
        contact.lastname=lastname
        contact.email=email
        contact.subject=subject
        contact.save()
    return render(request, 'thanks_contact.html')