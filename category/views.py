from django.shortcuts import render
from product.models import Category
from category.forms import CategoryEditForm, CategoryPostForm
from django.template.response import TemplateResponse
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def category_post(request):
    if request.method =='POST':
        form = CategoryPostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryPostForm(None)

    category=Category.objects.all()
    return TemplateResponse(request,'category/category_post.html',{'form':form,'category':category})



def category_edit(request, category_id):
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise Http404
        
    if request.method =="POST":
        form =CategoryEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category_post'))

    else:
        form = CategoryEditForm(instance=category)
    return TemplateResponse(request, 'category/category_edit.html',{'form': form, 'category': category})