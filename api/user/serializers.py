# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from api.user.models import Province, City, School, User


class ProvinceSerializer(ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
