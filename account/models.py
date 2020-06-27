from django.db import models

# Create your models here.
class Cart(models.Model):
    name = models.CharField("商品名", max_length=128)
    price = models.PositiveIntegerField("価格")
    count = models.PositiveIntegerField('数量')