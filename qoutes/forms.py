from django import forms
from .models import stock

class Stockform(forms.ModelForm):
    class Meta:
        model = stock
        fields = ['ticker',]
    
