# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from api.products.models import Products, ProductsCollect, ProductsMessage, ProductsClassification
from api.user.serializers import UserSerializer


class ProductsSerializer(ModelSerializer):
    create_user = UserSerializer()

    class Meta:
        model = Products
        fields = '__all__'


class ProductsCollectSerializer(ModelSerializer):
    class Meta:
        model = ProductsCollect
        fields = '__all__'


class ProductsMessageSerializer(ModelSerializer):
    create_user = UserSerializer()

    class Meta:
        model = ProductsMessage
        fields = '__all__'


class ProductsClassificationSerializer(ModelSerializer):
    class Meta:
        model = ProductsClassification
        fields = '__all__'
