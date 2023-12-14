from django.forms import TextInput
from.models import City
from django import forms

class Cityform(forms.ModelForm):
    class Meta:
        model=City
        fields=['name',]
        widgets={'name' : TextInput(attrs={'class':'form-control' ,'placeholder':"Enter a city/urban name"})}
