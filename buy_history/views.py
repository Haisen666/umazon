from django.shortcuts import render
from django.template.response import TemplateResponse
from buy.models import Buy
from ranking.models import Rank
from product.models import Product
from buy_history.models import BuyHistory

# Create your views here.
def buy_history(request):
    
    buy_history = BuyHistory.objects.filter(buy_history__user=request.user.id)
    

    return TemplateResponse(request,'buy_history/buy_history.html',{'rank':rank})
