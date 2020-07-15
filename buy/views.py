from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product
from django.template.response import TemplateResponse
from cart.models import Cart
from buy.models import Buy
from product.models import Product

# Create your views here.
def buy_list(request):

    cart = Cart.objects.filter(user=request.user.id)
    # buy = Buy.
    if request.method =='POST':
        count=0
        for c in cart:
            # product=Product.objects.get(id=c.product_num)
            # c.name=product.name
            # c.product_num = product.id
            buy = Buy()
            buy.user = request.user.id
            buy.product_num = c.product_num
            buy.price = c.price
            buy.count = c.count
            buy.total_price = c.price*c.count
            buy.save()
            count+=1

    if buy:
        # return HttpResponseRedirect(reverse('buy_list'))
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy,'count':count})
    else:
        return TemplateResponse(request,'top/toppage.html')