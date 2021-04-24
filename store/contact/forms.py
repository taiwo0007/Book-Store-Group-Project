from django import forms


class ContactForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea)
