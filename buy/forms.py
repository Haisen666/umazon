from django import forms
from buy.models import Buy

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = (
            'product_num',
            'name',
            'price',
            'count',
            'total_price',
        )