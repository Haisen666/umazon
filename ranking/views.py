from django.shortcuts import render
from django.template.response import TemplateResponse
from buy.models import Buy
from ranking.models import Rank
from product.models import Product

# Create your views here.
def ranking_list(request):
    
    rank = Rank.objects.order_by('buy_count').reverse()
        

    return TemplateResponse(request,'ranking/ranking_list.html',{'rank':rank})

