from .models import SystemUser, Worker
from rest_framework import serializers


class SystemUserSer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('user', 'department', 'name')


class WorkerSer(serializers.ModelSerializer):
    job = serializers.SlugRelatedField(
        slug_field='job_name',
        read_only=True
    )

    class Meta:
        model = Worker
        fields = '__all__'
