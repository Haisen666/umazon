from django.db import models
from cart.models import Cart

# Create your models here.
class Buy(models.Model):
    user = models.CharField('ユーザ',max_length=20)
    name = models.CharField("商品", max_length=128)
    product_num = models.CharField('商品番号', max_length=128, null=True, blank=True)
    price = models.PositiveIntegerField("価格")
    count = models.PositiveIntegerField('数量')
    total_price = models.PositiveIntegerField("合計",null=True, blank=True)
    buy_count = models.PositiveIntegerField("購入回数",null=True, blank=True)