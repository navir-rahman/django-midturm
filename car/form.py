from django import forms
from .models import CarModel, Comment

class QuantityUpdateForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['quantity']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'Comment'] 
