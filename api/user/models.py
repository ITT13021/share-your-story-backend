# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from api.common.models import AbstractAuditCreate


class Province(AbstractAuditCreate):
    name = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'省名'))

    class Meta:
        app_label = "user"
        db_table = "Province"


class City(AbstractAuditCreate):
    name = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'城市名'))
    province = models.ForeignKey(Province, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = "user"
        db_table = "city"


class School(AbstractAuditCreate):
    schoolname = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'学校名称'))
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        app_label = "user"
        db_table = "school"


class User(AbstractUser):
    SEX_CHOICES = ((0, '保密'), (1, '男'), (2, '女'))
    AUTHORITY_CHOICES = ((0, '普通用户'), (1, '管理员'), (2, '超级管理员'))
    username = models.CharField(max_length=20, blank=True, null=True, unique=True, help_text=_(u'用户名'))  # 覆盖，允许重复
    cellphone = models.CharField(max_length=20, blank=True, null=True, help_text=_(u'手机号码'))
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=0, help_text=_(u'性别'))
    signature = models.CharField(max_length=30, blank=True, null=True, help_text=_(u'签名'))
    school = models.ForeignKey(School, models.DO_NOTHING, blank=True, null=True)
    authority = models.SmallIntegerField(choices=AUTHORITY_CHOICES, default=0, help_text=_(u'权限'))

    class Meta:
        app_label = "user"
        db_table = "user"
