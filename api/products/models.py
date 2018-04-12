# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext_lazy as _

from api.user.models import User


class AbstractAuditCreate(models.Model):
    # from api.user.models import User
    create_user = models.ForeignKey(User, models.DO_NOTHING, related_name='%(app_label)s_%(class)s_create_user_set', blank=True, null=True, help_text=_(u'创建人'))
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text=_(u'创建时间'))

    class Meta:
        abstract = True


class ProductsClassification(AbstractAuditCreate):
    name = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'分类名称'))

    class Meta:
        app_label = 'products'
        db_table = 'Products_classification'


class Products(AbstractAuditCreate):
    name = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'商品名'))
    price = models.IntegerField(blank=True, null=True, help_text=_(u'出售价格'))
    description = models.TextField(blank=True, null=True, help_text=_(u'商品描述'))
    views = models.IntegerField(blank=True, null=True, help_text=_(u'浏览次数'))
    buy_price = models.IntegerField(blank=True, null=True, help_text=_(u'购买价格'))
    classification = models.ForeignKey(ProductsClassification, models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True, help_text=_(u'状态{0：上架, 1: 下架}'))

    class Meta:
        app_label = 'products'
        db_table = 'products'


class ProductsCollect(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'products'
        db_table = 'products_collect'


class ProductsMessage(AbstractAuditCreate):
    message = models.CharField(max_length=200, blank=True, null=True, help_text=_(u'商品留言'))
    parent_message = models.IntegerField(blank=True, null=True, help_text=_(u'父级留言'))
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'products'
        db_table = 'products_message'


