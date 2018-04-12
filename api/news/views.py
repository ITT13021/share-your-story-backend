# -*- coding: utf-8 -*-
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet

from api.news.models import News, NewsClassification
from api.news.serializers import NewsSerializer, NewsClassificationSerializer


@permission_classes((permissions.AllowAny,))
class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsClassificationView(ModelViewSet):
    queryset = NewsClassification.objects.all()
    serializer_class = NewsClassificationSerializer
