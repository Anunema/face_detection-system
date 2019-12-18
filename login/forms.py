from django import forms

class Registration(forms.Form):
    username = forms.CharField(max_length=30)