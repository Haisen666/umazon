from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product
from django.template.response import TemplateResponse
from cart.models import Cart
from product.models import Product

# Create your views here.
def buy_list(request):
    cart = Cart.objects.filter(user=request.user.id)
    i=[]
    money=0
    for c in cart:
        product=Product.objects.get(id=c.product_num)
        c.name=product.name
        c.product_num = product.id
        i.append(c.price*c.count)

    c=len(i)     
    money=sum(i)
    if cart:
        return TemplateResponse(request,'buy/buy_list.html',{'cart':cart,'i':i,'c':c,'money':money})
    else:
        return TemplateResponse(request,'top/toppage.html')