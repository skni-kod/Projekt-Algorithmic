from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='User name', max_length=100)