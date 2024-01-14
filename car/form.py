from django import forms
from .models import CarModel

class QuantityUpdateForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['quantity']
