# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from api.common.mixins import AuditSerializerMixin
from api.news.models import NewsClassification, News
from api.user.serializers import UserSerializer


class NewsSerializer(AuditSerializerMixin, ModelSerializer):
    create_user = UserSerializer(read_only=True)

    class Meta:
        model = News
        fields = '__all__'


class NewsClassificationSerializer(ModelSerializer):
    class Meta:
        model = NewsClassification
        fields = '__all__'
