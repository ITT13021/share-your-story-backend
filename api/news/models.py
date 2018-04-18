# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext_lazy as _
from api.user.models import User


class AbstractAuditCreate(models.Model):
    create_user = models.ForeignKey(User, models.DO_NOTHING, related_name='%(app_label)s_%(class)s_create_user_set', blank=True, null=True, help_text=_(u'创建人'))
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text=_(u'创建时间'))

    class Meta:
        abstract = True


class News(AbstractAuditCreate):
    title = models.CharField(blank=True, null=True, max_length=12, help_text=_(u'消息标题'))
    content = models.TextField(blank=True, null=True, help_text=_(u'消息内容'))

    class Meta:
        app_label = 'news'
        db_table = 'news'


class UserNews(models.Model):
    TYPE_CHOICES = ((0, "全体用户"), (1, "部分用户"))

    news = models.ForeignKey(News)
    user = models.ForeignKey(User, blank=True, null=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES, blank=True, null=True, help_text=_(u'消息范围'))
    read = models.BooleanField(default=False)

    class Meta:
        app_label = 'news'
        db_table = 'user_news'
