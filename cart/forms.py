from django import forms
from cart.models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = (
            'product_num',
            'name',
            'price',
            'count',
        )
