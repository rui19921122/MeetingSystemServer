from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import ChangePasswordSer


# Create your views here.
class BaseLoginInView(APIView):
    """
    基本登陆模块，由于还有指纹登陆的方式，因此取名为base-login
    """
    serializer_class = AuthTokenSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({'status': 'success'})


class LoginOutView(APIView):
    """
    登出
    """

    def post(self, request: HttpRequest):
        logout(request)
        return Response({'status': 'success'})


class ChangePasswordView(APIView):
    """
    更改密码
    """
    serializer_class = ChangePasswordSer

    def post(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        request.user.set_password(password)
        request.user.save()
        return Response({'status': 'success'})
