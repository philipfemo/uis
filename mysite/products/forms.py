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
            "category",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "category",
        ]
class ProducStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "stock"
        ]


#products = Product.objects.values('surname', 'name')
#StockFormSet = modelformset_factory(stock, extra=len(products)
