from django.db import models
from product.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.CharField('ユーザ',max_length=20)
    # category = models.CharField('カテゴリー', max_length=128,blank=True, null=True)
    name = models.CharField("商品", max_length=128)
    product_num = models.CharField('商品番号', max_length=128, null=True, blank=True)
    # image = models.ImageField(upload_to='images',blank=True, null=True)
    price = models.PositiveIntegerField("価格")
    count = models.PositiveIntegerField('数量')