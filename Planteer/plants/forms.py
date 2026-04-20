from django import forms
from django.core.exceptions import ValidationError

from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ["name", "about", "used_for", "category", "is_edible", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Plant name", "required": True, "minlength": "2", "maxlength": "256"}
            ),
            "about": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "About this plant", "required": True, "minlength": "10"}
            ),
            "used_for": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "What is this plant used for?",
                    "required": True,
                    "minlength": "10",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select", "required": True}),
            "is_edible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 2:
            raise ValidationError("Plant name must be at least 2 characters.")
        return name

    def clean_about(self):
        about = self.cleaned_data.get("about", "").strip()
        if len(about) < 10:
            raise ValidationError("About must be at least 10 characters.")
        return about

    def clean_used_for(self):
        used_for = self.cleaned_data.get("used_for", "").strip()
        if len(used_for) < 10:
            raise ValidationError("Used For must be at least 10 characters.")
        return used_for

    def clean_category(self):
        category = self.cleaned_data.get("category", "")
        valid = [c[0] for c in Plant.category.field.choices]
        if category not in valid:
            raise ValidationError("Please select a valid category.")
        return category
