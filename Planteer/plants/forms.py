from django import forms

from .models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ["name", "about", "used_for", "category", "is_edible", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Plant name"}
            ),
            "about": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "About this plant"}
            ),
            "used_for": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "What is this plant used for?",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "is_edible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
