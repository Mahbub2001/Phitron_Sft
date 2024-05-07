from django import forms
from . models import Album

class ADD_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'



class Edit_Album(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'