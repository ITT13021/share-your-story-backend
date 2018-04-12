# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.products.models import Products, ProductsClassification, ProductsCollect, ProductsMessage
from api.products.serializers import ProductsSerializer, ProductsClassificationSerializer, ProductsCollectSerializer, ProductsMessageSerializer


class CustomizeSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 20


@permission_classes((permissions.AllowAny,))
class ProductsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request, *args, **kwargs):
        return super(ProductsView, self).list(request, *args, **kwargs)


class ProductsClassificationView(ModelViewSet):
    queryset = ProductsClassification.objects.all()
    serializer_class = ProductsClassificationSerializer


class ProductsCollectView(ModelViewSet):
    queryset = ProductsCollect.objects.all()
    serializer_class = ProductsCollectSerializer
    pagination_class = CustomizeSetPagination

    def list(self, request, *args, **kwargs):
        self.queryset = ProductsCollect.objects.filter(user=request.user).all()
        return super(ProductsCollectView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        product = request.data.get('product', None)
        user = request.data.get('user', None)
        res = ProductsCollect.objects.filter(product=product, user=user).exists()
        if res:
            return JsonResponse({'msg': '已经收藏过啦， 不用再收藏了！', 'status': 400})
        return super(ProductsCollectView, self).create(request, *args, **kwargs)


@permission_classes((permissions.IsAuthenticated,))
class ProductsMessageView(ModelViewSet):
    queryset = ProductsMessage.objects.all()
    serializer_class = ProductsMessageSerializer

    def list(self, request, *args, **kwargs):
        product = request.GET.get('product', None)
        self.queryset = ProductsMessage.objects.filter(product=product)
        return super(ProductsMessageView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ProductsMessageView, self).create(request, *args, **kwargs)
