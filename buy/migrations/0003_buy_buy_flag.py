# Generated by Django 3.0.2 on 2020-07-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_buy_buy_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='buy_flag',
            field=models.BooleanField(default=False, verbose_name='購入結果'),
        ),
    ]
