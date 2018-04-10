# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-08 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('name', models.CharField(blank=True, help_text='\u5546\u54c1\u540d', max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, help_text='\u51fa\u552e\u4ef7\u683c', null=True)),
                ('description', models.TextField(blank=True, help_text='\u5546\u54c1\u63cf\u8ff0', null=True)),
                ('views', models.IntegerField(blank=True, help_text='\u6d4f\u89c8\u6b21\u6570', null=True)),
                ('buy_price', models.IntegerField(blank=True, help_text='\u8d2d\u4e70\u4ef7\u683c', null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductsClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('name', models.CharField(blank=True, help_text='\u5206\u7c7b\u540d\u79f0', max_length=20, null=True)),
                ('create_user', models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products_productsclassification_create_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Products_classification',
            },
        ),
        migrations.CreateModel(
            name='ProductsCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products_collect',
            },
        ),
        migrations.CreateModel(
            name='ProductsMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('message', models.CharField(blank=True, help_text='\u5546\u54c1\u7559\u8a00', max_length=200, null=True)),
                ('parent_message', models.IntegerField(blank=True, help_text='\u7236\u7ea7\u7559\u8a00', null=True)),
                ('create_user', models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products_productsmessage_create_user_set', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
            ],
            options={
                'db_table': 'products_message',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductsClassification'),
        ),
        migrations.AddField(
            model_name='products',
            name='create_user',
            field=models.ForeignKey(blank=True, help_text='\u521b\u5efa\u4eba', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='products_products_create_user_set', to=settings.AUTH_USER_MODEL),
        ),
    ]