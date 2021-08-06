from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "description": forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
            "image": forms.FileInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "price": forms.NumberInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            "category": forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            "created_at": forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                },
            ),
        }