from django import forms
from product.models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'count',
        )

class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'price',
            'count',
        )