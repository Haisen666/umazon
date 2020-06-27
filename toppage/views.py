from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.template.response import TemplateResponse
from product.models import Product
from product.forms import ProductSearchForm
from rest_framework import generics, permissions


# Create your views here.

def top(request):
    products = Product.objects.order_by('name')
    form = ProductSearchForm(request.GET)
    products = form.filter_products(products)
    
    params = request.GET.copy()
    if 'page' in params:
        page = params['page']
        del params['page']
    else:
        page = 1
    search_params = params.urlencode()


    paginator = Paginator(products, 5)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except (EmptyPage, PageNotAnInteger):
        products = paginator.page(1)
    return TemplateResponse(request,'top/toppage.html',{'products': products,'form': form,'search_params': search_params})




        


# def product_post(request):
    
#     if request.method =='POST':
#         form=ProductEditForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=ProductEditForm(None)

#     product=Product.objects.all()
#     return TemplateResponse(request,'top/product_edit.html',{'form':form,'product':product,'propro':propro})

