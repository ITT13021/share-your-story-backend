# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from api.user.models import Province


class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
