# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from api.common.mixins import AuditSerializerMixin
from api.products.models import Products, ProductsCollect, ProductsMessage, ProductsClassification
from api.user.serializers import UserSerializer


class ProductsSerializer(AuditSerializerMixin, ModelSerializer):
    create_user = UserSerializer(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'


class ProductsCollectSerializer(ModelSerializer):
    product_info = ProductsSerializer(source="product", read_only=True)

    class Meta:
        model = ProductsCollect
        fields = '__all__'


class ProductsMessageSerializer(AuditSerializerMixin, ModelSerializer):
    create_user = UserSerializer(read_only=True)

    class Meta:
        model = ProductsMessage
        fields = '__all__'


class ProductsClassificationSerializer(ModelSerializer):
    class Meta:
        model = ProductsClassification
        fields = '__all__'
