from django import forms
from cart.models import Cart

class CartEditForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = (
            'name',
            'price',
            'count',
        )

class CartPostForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = (
            'name',
            'price',
            'count',
        )