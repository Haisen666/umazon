from django import forms
from toppage.models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'price',
            'count',
        )