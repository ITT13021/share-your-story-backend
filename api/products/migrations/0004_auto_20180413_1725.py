# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-13 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(blank=True, default=0, help_text='\u72b6\u6001{0\uff1a\u4e0a\u67b6, 1: \u4e0b\u67b6}', max_length=5, null=True),
        ),
    ]