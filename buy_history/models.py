from django.db import models
from buy.models import Buy

# Create your models here.
class BuyHistory(models.Model):
    buy_history = models.ForeignKey(Buy,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField("購入日付")

