from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product
from django.template.response import TemplateResponse
from cart.models import Cart
from cart.forms import CartForm


# Create your views here.
@require_POST
def cart_add(request, product_id):
    if not Product.objects.filter(id=product_id).exists():
        raise Http404
    
    if request.method =='POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cart = Cart()
            cart.user = request.user.id
            cart.name = product_id
            cart.price = request.POST['price']
            cart.count = request.POST['count']
            cart.save()
    else:
        form = CartForm()
    return TemplateResponse(request,'top/toppage.html')


def cart_list(request):
    cart = Cart.objects.filter(user=request.user.id)
    # cart = Cart.objects.all()
    if cart:
        return TemplateResponse(request,'cart/cart_list.html',{'cart':cart})
    else:
        return TemplateResponse(request,'top/toppage.html')

