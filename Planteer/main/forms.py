from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "message"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "contact-input",
                "placeholder": "John",
                "required": True,
                "minlength": "2",
                "maxlength": "256",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "contact-input",
                "placeholder": "Doe",
                "required": True,
                "minlength": "2",
                "maxlength": "256",
            }),
            "email": forms.EmailInput(attrs={
                "class": "contact-input",
                "placeholder": "john.doe@example.com",
                "required": True,
            }),
            "message": forms.Textarea(attrs={
                "class": "contact-input contact-textarea",
                "placeholder": "Write your message here...",
                "required": True,
                "minlength": "10",
            }),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", "").strip()
        if len(first_name) < 2:
            raise ValidationError("First name must be at least 2 characters.")
        if not first_name.isalpha():
            raise ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", "").strip()
        if len(last_name) < 2:
            raise ValidationError("Last name must be at least 2 characters.")
        if not last_name.isalpha():
            raise ValidationError("Last name must contain only letters.")
        return last_name

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()
        if len(message) < 10:
            raise ValidationError("Message must be at least 10 characters.")
        return message
