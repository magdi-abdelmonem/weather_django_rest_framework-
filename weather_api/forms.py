from pyexpat import model
from .models import weather
from django import forms

class Weatherform(forms.ModelForm):
    class Meta:
        model=weather
        fields=['city_name']

        widgets={

            'city_name':forms.TextInput(attrs={'class':'form-control'})

        }