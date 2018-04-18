# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.user.serializers import *
from rest_framework.authtoken.models import Token


class ProvinceView(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def list(self, request, *args, **kwargs):
        return super(ProvinceView, self).list(request, *args, **kwargs)


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):
        province = request.GET.get("province", None)
        self.queryset = City.objects.filter(province=province).all()
        return super(CityView, self).list(request, *args, **kwargs)


class SchoolView(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def list(self, request, *args, **kwargs):
        city = request.GET.get("city", None)
        self.queryset = School.objects.filter(city=city).all()
        return super(SchoolView, self).list(request, *args, **kwargs)


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        password = request.data.get('password', None)
        username = request.data.get('username', None)
        user = self.get_user_or_create_new(username, password)  # 查找或注册新用户
        return self.get_authcheckinfo(user)

    def get_user_or_create_new(self, username, password):
        user = authenticate(username=username, password=password)
        if user is None:
            user_test = User.objects.filter(username=username).first()
            if user_test is None:
                username = self.request.data.get('username', None)
                cellphone = self.request.data.get('cellphone', None)
                User.objects.create(username=username, password=make_password(password), cellphone=cellphone, is_staff=True)
                user = authenticate(username=username, password=password)
            else:
                user = user_test
        return user

    def res(self, msg=None, usrname=None, status=status.HTTP_200_OK):
        if msg is not None:
            return Response({'msg': msg}, status)
        rst = {'usrname': usrname}
        print rst
        return Response(rst, status=status)

    def get_authcheckinfo(self, user):
        token = Token.objects.get_or_create(user=user)[0].key  # 创建token
        return self.res(usrname=user.username, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        return super(UserView, self).update(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)
    token = Token.objects.get_or_create(user=user)[0].key  # 创建token
    user_information = json.dumps({"id": user.id, "username": user.username, "is_superuser": user.is_superuser,
                                   "date_joined": user.date_joined.strftime('%Y-%m-%d'), "cellphone": int(user.cellphone),
                                   "sex": user.sex, "school": user.school.schoolname, "signature": user.signature,
                                   "token": token, "school_id": user.school.id, "school_name": user.school.schoolname,
                                    "city_id": user.school.city.id, "city_name": user.school.city.name,
                                   "province_id": user.school.city.province.id, "province_name": user.school.city.province.name})
    if user:
        return JsonResponse({'msg': '验证成功', 'token': token, 'user': user_information, 'status': 200})
    else:
        return JsonResponse({'msg': '验证失败', 'status': 401})
