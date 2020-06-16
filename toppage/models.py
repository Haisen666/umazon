from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("カテゴリー名", max_length=32)
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.SET_NULL)
    name = models.CharField("商品名", max_length=128)
    price = models.PositiveIntegerField("価格")
    count = models.PositiveIntegerField('数量')