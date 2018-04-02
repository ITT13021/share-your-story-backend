# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from api.user.models import Province
from api.user.serializers import ProvinceSerializer


class ProvinceView(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
