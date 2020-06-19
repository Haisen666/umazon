from django.shortcuts import render
from django.template.response import TemplateResponse
from toppage.models import Product


# Create your views here.
def top(request):
    products = Product.objects.order_by('name')
    return render(request,'top/toppage.html',{'products': products})



def product_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    return TemplateResponse(request,'top/product_detail.html',{'product': product})

