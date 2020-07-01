"""umazon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import account.views
import toppage.views
import product.views
import category.views
import cart.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',toppage.views.top,name='toppage'),
    path('', include('account.urls')),
    # path('user_index/', account.views.user_index,name='user_index'),
    path('products/<int:product_id>',product.views.product_detail,name='product_detail'),
    path('products/<int:product_id>/edit/', product.views.product_edit,name='product_edit'),
    path('products/<int:product_id>/delete/',product.views.product_delete,name='product_delete'),
    path('products/post/',product.views.product_post,name='product_post'),
    path('category/<int:category_id>/edit/', category.views.category_edit,name='category_edit'),
    path('category/post/',category.views.category_post,name='category_post'),
    path('cart/<int:product_id>/add/', cart.views.cart_add, name='cart_add'),
]
