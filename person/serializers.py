from .models import SystemUser
from rest_framework import serializers


class SystemUserSer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('user', 'department', 'name')

