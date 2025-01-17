from django import forms
from .models import Contact
from django.forms import widgets


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        exclude = ()


        widgets  = {
            'name ':widgets.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name'}),
            'email ':widgets.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
            'phone ':widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Your Phone Number'}),
            'message ':widgets.Textarea(attrs={'class': 'form-control', 'placeholder':'Your Message'})
        }