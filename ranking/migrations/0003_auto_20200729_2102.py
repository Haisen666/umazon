# Generated by Django 3.0.2 on 2020-07-29 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_buy_buy_flag'),
        ('ranking', '0002_auto_20200729_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='product_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Buy'),
        ),
    ]