from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product

# Create your views here.
@require_POST
def cart_add(request, product_id):
    if not Product.objects.filter(id=product_id).exists():
        raise Http404
    
    
    cart = request.session.get('cart')
    if cart:
        cart.append(product_id)
        request.session['cart'] = cart
    else:
        request.session['cart'] = [product_id]
    return HttpResponseRedirect(reverse('toppage'))

