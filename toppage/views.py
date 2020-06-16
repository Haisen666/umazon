from django.shortcuts import render
from django.template.response import TemplateResponse
from toppage.models import Product

def product_list(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request, 'top/toppage.html',{'products': products})

# Create your views here.
def top(request):
    return render(request,'top/toppage.html')

