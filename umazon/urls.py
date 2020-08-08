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
from django.contrib.auth.models import User
import account.views
import toppage.views
import product.views
import category.views
import cart.views
import buy.views
import ranking.views
import buy_history.views
import contact.views
from django.conf.urls.static import static
from umazon import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',toppage.views.top,name='toppage'),
    path('', include('account.urls')),
    path('user_index/', account.views.user_index,name='user_index'),
    path('products/<int:product_id>',product.views.product_detail,name='product_detail'),
    path('products/<int:product_id>/edit/', product.views.product_edit,name='product_edit'),
    path('products/<int:product_id>/delete/',product.views.product_delete,name='product_delete'),
    path('products/post/',product.views.product_post,name='product_post'),
    path('category/<int:category_id>/edit/', category.views.category_edit,name='category_edit'),
    path('category/post/',category.views.category_post,name='category_post'),
    path('cart/<int:product_id>/add/', cart.views.cart_add, name='cart_add'),
    path('cart/list/', cart.views.cart_list, name='cart_list'),
    path('cart/<int:id>/edit/', cart.views.cart_edit, name='cart_edit'),
    path('buy/', buy.views.buy_post, name='buy_post'),
    path('buy_list/', buy.views.buy_list, name='buy_list'),
    path('cart/<int:id>/delete', cart.views.cart_delete, name='cart_delete'),
    path('buy_action/', buy.views.buy_action, name='buy_action'),
    path('ranking_list/', ranking.views.ranking_list, name='ranking_list'),
    path('buy_history/', buy_history.views.buy_history, name='buy_history'),
    path('', include('contact.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)