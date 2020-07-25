from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product
from django.template.response import TemplateResponse
from cart.models import Cart
from buy.models import Buy
from product.models import Product
from buy.forms import BuyForm
# Create your views here.

def buy_list(request):
    buy=Buy.objects.filter(user=request.user.id)
    
    if buy:
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy})
    else:
        return TemplateResponse(request,'top/toppage.html')



def buy_post(request):
    try:
        cart=Cart.objects.filter(user=request.user.id)
    except Cart.DoesNotExist:
        raise Http404
    
    buy = Buy()
    if request.method =='POST':
        for c in cart:
            form = BuyForm(request.POST)
            if form.is_valid():
                buy.user = request.user.id
                buy.product_num = c.product_num
                buy.name = c.name
                buy.price = c.price
                buy.count = c.count
                buy.total_price = c.price*c.count
                buy.buy_count = 1
                buy.save()
            else:
                form = BuyForm(None)

                
        cart.delete()
        buy=Buy.objects.filter(user=request.user.id)
    if buy:
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy})
       
    else:
        return TemplateResponse(request,'top/toppage.html')