from rest_framework import serializers


class ChangePasswordSer(serializers.Serializer):
    password = serializers.CharField(max_length=10, min_length=4)
