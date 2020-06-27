from django.shortcuts import render
from django.template.response import TemplateResponse
from product.models import Category, Product
from django.http import Http404
from django.http.response import HttpResponseRedirect
from product.forms import ProductEditForm, ProductPostForm
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
propro="他の商品登録はこちらどうぞ"
def product_post(request):
    if request.user.has_perm('accounts.admin'):
        if request.method =='POST':
            form=ProductPostForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form=ProductPostForm(None)

        product=Product.objects.all()
        category=Category.objects.all()
        return TemplateResponse(request,'product/product_post.html',{'form':form,'product':product,'propro':propro,'category':category})
    else:
        return TemplateResponse(request,'top/toppage.html')


def product_detail(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    return TemplateResponse(request,'product/product_detail.html',{'product': product})

def product_edit(request, product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
        
    if request.user.has_perm('accounts.admin'):
        if request.method =="POST":
            form =ProductEditForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('product_detail',args=(product.id,)))

        else:
            form = ProductEditForm(instance=product)
        return TemplateResponse(request, 'product/product_edit.html',{'form': form, 'product': product})

    else:
        return TemplateResponse(request,'top/toppage.html')


def product_delete(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    if request.user.has_perm('accounts.admin'):   
        if request.method == "POST":
            product.delete()
            return HttpResponseRedirect(reverse('product_list'))
        else:
            return TemplateResponse(request, 'product/product_delete.html',{'product': product})
    else:
        return TemplateResponse(request,'top/toppage.html')