from django import forms
from django.forms import widgets

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Name"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "form-control", "placeholder": "Your Email"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "form-control", "placeholder": "Your Phone Number"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "form-control", "placeholder": "Your Message"}
            ),
        }
