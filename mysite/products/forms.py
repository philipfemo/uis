from django import forms

from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "stock",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "category",
        ]
