# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from api.products.models import Products, ProductsClassification, ProductsCollect, ProductsMessage
from api.products.serializers import ProductsSerializer, ProductsClassificationSerializer, ProductsCollectSerializer, ProductsMessageSerializer


class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsClassificationView(ModelViewSet):
    queryset = ProductsClassification.objects.all()
    serializer_class = ProductsClassificationSerializer


class ProductsCollectView(ModelViewSet):
    queryset = ProductsCollect.objects.all()
    serializer_class = ProductsCollectSerializer


class ProductsMessageView(ModelViewSet):
    queryset = ProductsMessage.objects.all()
    serializer_class = ProductsMessageSerializer

    def list(self, request, *args, **kwargs):
        product = request.GET.get('product', None)
        self.queryset = ProductsMessage.objects.filter(product=product)
        return super(ProductsMessageView, self).list(request, *args, **kwargs)




