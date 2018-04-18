# -*- coding: utf-8 -*-
from django.db.models import Q
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.news.models import News, UserNews
from api.news.serializers import NewsSerializer, UserNewsSerializer


class MyNewsCustomizeSetPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 20


@permission_classes((permissions.AllowAny,))
class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        self.pagination_class = MyNewsCustomizeSetPagination
        new_ids = UserNews.objects.filter(Q(type=0) | Q(user=request.user)).values_list("news", flat=True)
        self.queryset = News.objects.filter(pk__in=new_ids)
        return super(NewsView, self).list(request, *args, **kwargs)


class UserNewsView(ModelViewSet):
    queryset = UserNews.objects.all()
    serializer_class = UserNewsSerializer
