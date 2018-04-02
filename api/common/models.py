# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext_lazy as _


class AbstractAuditCreate(models.Model):
    # from api.user.models import User
    create_user = models.ForeignKey('User', models.DO_NOTHING, related_name='%(app_label)s_%(class)s_create_user_set', blank=True, null=True, help_text=_(u'创建人'))
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text=_(u'创建时间'))

    class Meta:
        abstract = True
