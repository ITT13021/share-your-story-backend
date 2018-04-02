# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.user.models import Province, School, City, User
from api.user.serializers import *
from rest_framework.authtoken.models import Token


class ProvinceView(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SchoolView(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        password = request.POST.get("password", 'abc.123')
        username = request.POST.get("username")
        user = self.get_user_or_create_new(username, password)  # 查找或注册新用户
        return self.get_authcheckinfo(user)

    def get_user_or_create_new(self, imid, password):
        user = authenticate(username=imid, password=password)
        if user is None:
            username = self.request.POST.get('username', None)
            cellphone = self.request.POST.get('cellphone', None)
            User.objects.create(username=username, password=make_password(password), cellphone=cellphone, is_staff=True)
            user = authenticate(username=imid, password=password)
        return user

    def res(self, msg=None, usrid=None, usrname=None, cellphone=None, token=None, status=status.HTTP_200_OK):
        if msg is not None:
            return Response({'msg': msg}, status)
        rst = {'usrid': usrid, 'usrname': usrname, 'cellphone': cellphone, 'token': token}
        print rst
        return Response(rst, status=status)

    def get_authcheckinfo(self, user):
        token = Token.objects.get_or_create(user=user)[0].key  # 创建token
        return self.res(usrid=user.id, usrname=user.username, cellphone=user.cellphone, token=token, status=status.HTTP_200_OK)
