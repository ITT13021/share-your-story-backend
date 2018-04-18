# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from api.common.mixins import AuditSerializerMixin
from api.news.models import News, UserNews
from api.user.serializers import UserSerializer


class NewsSerializer(AuditSerializerMixin, ModelSerializer):
    create_user = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class UserNewsSerializer(ModelSerializer):
    class Meta:
        model = UserNews
        fields = '__all__'
