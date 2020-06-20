from django.shortcuts import render
from django.template.response import TemplateResponse
from product.models import Product



# Create your views here.

def top(request):
    products = Product.objects.order_by('name')
    return TemplateResponse(request,'top/toppage.html',{'products': products})




        


# def product_post(request):
    
#     if request.method =='POST':
#         form=ProductEditForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=ProductEditForm(None)

#     product=Product.objects.all()
#     return TemplateResponse(request,'top/product_edit.html',{'form':form,'product':product,'propro':propro})

