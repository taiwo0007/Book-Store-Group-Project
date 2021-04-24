from django import forms
from django.forms import ModelForm
from .models import Voucher


class VoucherApplyForm(forms.Form):
    code = forms.CharField()



class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = '__all__'