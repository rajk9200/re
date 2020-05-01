
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control',

        'autocomplete' : "on"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'autocomplete' : "on"
    }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'autocomplete': "off",
        'cols' : "10",
        'rows':'2',

    }))