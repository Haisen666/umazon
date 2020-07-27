from django.shortcuts import render
from django.template.response import TemplateResponse
from buy.models import Buy
from product.models import Product

# Create your views here.
def ranking_list(request):
    rank = []
    buy = Buy.objects.order_by('buy_count')
    for b in buy:
        count=1
        rank.append(count)
        count += 1

    return TemplateResponse(request,'ranking/ranking_list.html',{'buy':buy,'rank':rank})

