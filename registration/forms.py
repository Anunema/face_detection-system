from django import forms
from . import models

class Registration(forms.ModelForm):
    class Meta:
        model = models.user
        fields = ('username', 'first_name', 'last_name','email')