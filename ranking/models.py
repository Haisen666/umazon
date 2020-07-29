from django.db import models
from buy.models import Buy

# Create your models here.
class Rank(models.Model):
    product_num = models.ForeignKey(Buy,on_delete=models.CASCADE,null=True)
    buy_count = models.PositiveIntegerField('購入回数',default=0)

