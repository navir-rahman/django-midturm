from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        
        if instance:
            self.fields['username'].initial = instance.username
            self.fields['email'].initial = instance.email
            self.fields['first_name'].initial = instance.first_name
            self.fields['last_name'].initial = instance.last_name

    def save(self, commit=True, *args, **kwargs):
        return super().save(commit=commit, *args, **kwargs)
