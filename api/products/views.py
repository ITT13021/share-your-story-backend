# -*- coding: utf-8 -*-
from itertools import chain

import itertools
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('classification',)
    search_fields = ('name',)

    def list(self, request, *args, **kwargs):
        type = request.GET.get("type", None)
        if type == 'my':
            self.pagination_class = CustomizeSetPagination
            self.queryset = Products.objects.filter(create_user=request.user)
        elif type == 'recommend':
            self.queryset = Products.objects.filter(status=0).order_by('-create_date').all()[:5]
        elif type == 'home':
            self.pagination_class = None
            books = Products.objects.filter(classification=2, status=0).all()[:12].values_list('id', flat=True)
            electric = Products.objects.filter(classification=1, status=0).all()[:12].values_list('id', flat=True)
            other = Products.objects.filter(classification=3, status=0).all()[:12].values_list('id', flat=True)
            ids = [i for i in books] + [i for i in electric]+ [i for i in other]
            self.queryset = Products.objects.filter(pk__in=ids).all()
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


class ProductsMessageView(ModelViewSet):
    queryset = ProductsMessage.objects.all()
    serializer_class = ProductsMessageSerializer

    def list(self, request, *args, **kwargs):
        product = request.GET.get('product', None)
        self.queryset = ProductsMessage.objects.filter(product=product)
        return super(ProductsMessageView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ProductsMessageView, self).create(request, *args, **kwargs)
