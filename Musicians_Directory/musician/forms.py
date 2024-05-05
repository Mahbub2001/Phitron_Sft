from django import forms
from .models import Musician

class ad_mus(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

class ed_mus(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']
