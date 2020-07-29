from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from product.models import Product
from django.template.response import TemplateResponse
from cart.models import Cart
from buy.models import Buy
from ranking.models import Rank
from product.models import Product
from buy.forms import BuyForm
# Create your views here.

def buy_list(request):
    buy=Buy.objects.filter(user=request.user.id)
    kensu=0
    money=0
    for b in buy:
        if b.buy_flag == False:
            kensu += 1
            money += b.total_price
    money = int(money*1.1)
    
    if buy:
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy,'kensu':kensu,'money':money})
    else:
        return TemplateResponse(request,'top/toppage.html')



def buy_post(request):
    try:
        cart=Cart.objects.filter(user=request.user.id)
    except Cart.DoesNotExist:
        raise Http404
    
    if request.method =='POST':
        for c in cart:
            form = BuyForm(request.POST)
            if form.is_valid():
                buy = Buy()
                buy.user = request.user.id
                buy.product_num = c.product_num
                buy.name = c.name
                buy.price = c.price
                buy.count = c.count
                buy.total_price = c.price*c.count
                if buy.buy_count == "" or buy.buy_count == None:
                    buy.buy_count = 1
                else:
                    buy.buy_count = buy.buy_count+1
                buy.save()
            else:
                form = BuyForm(None)


        cart.delete()
        buy=Buy.objects.filter(user=request.user.id)
        kensu=0
        money=0
        for b in buy:
            if b.buy_flag == False:
                kensu += 1
                money += b.total_price
        money= int(money*1.1)

    if buy:
        return TemplateResponse(request,'buy/buy_list.html',{'buy':buy,'kensu':kensu,'money':money})
       
    else:
        return TemplateResponse(request,'top/toppage.html')

    
def buy_action(request):
    try:
        buy=Buy.objects.filter(user=request.user.id)
    except Buy.DoesNotExist:
        raise Http404

    if request.method =='POST':
        for b in buy:
            if b.buy_flag == False:
                product = Product.objects.get(id = b.product_num)
                product.count = product.count - b.count
                product.save()

                b.buy_flag = True
                rank=Rank()
                rank.product_num = b
                rank.buy_count = rank.buy_count+b.count
                rank.save()

                b.save()
        return TemplateResponse(request,'top/toppage.html')
    else:
        return TemplateResponse(request,'top/toppage.html')
