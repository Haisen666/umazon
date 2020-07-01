from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm
from product.models import Product
from product.forms import ProductSearchForm
from django.template.response import TemplateResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'


def user_index(request):
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
    # products = Product.objects.order_by('name')
    # return render(request,'top/toppage.html',{'products': products})