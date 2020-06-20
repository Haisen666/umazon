from django import forms
from product.models import Category, Product

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )

class CategoryPostForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )