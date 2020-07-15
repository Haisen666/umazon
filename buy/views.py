from django.shortcuts import render
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

    cart = Cart.objects.filter(user=request.user.id)

    if request.method =='POST':
        count=0
        for c in cart:
            form = BuyForm(request.POST)
            if form.is_valid():
                buy = Buy()
                buy.user = request.user.id
                buy.product_num = c.product_num
                buy.price = c.price
                buy.count = c.count
                buy.total_price = c.price*c.count
                buy.save()
                count+=1
        else:
            form = BuyForm(None)
    # buy = Buy.
    
    buy=Buy.objects.all()
    if buy:
        # return HttpResponseRedirect(reverse('buy_list'),{'buy':buy,'count':count})
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy,'count':count})
    else:
        return TemplateResponse(request,'top/toppage.html')