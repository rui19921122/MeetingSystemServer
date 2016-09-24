from rest_framework import serializers
from person.models import Worker
from .models import AttendPerson, AttendTable


class AttendPersonSer(serializers.HyperlinkedModelSerializer):
    job = serializers.SlugRelatedField(
        slug_field='job_name',
        read_only=True
    )
    worker = serializers.SlugRelatedField(
        slug_field='worker_name',
        read_only=True
    )
    url = serializers.HyperlinkedIdentityField(view_name='change-worker')
    off_record = serializers.SlugRelatedField(slug_field='time', read_only=True)
    on_record = serializers.SlugRelatedField(slug_field='time', read_only=True)

    class Meta:
        model = AttendPerson
        fields = ['off_record', 'on_record', 'url', 'job', 'worker','is_study']


class AttendTableSer(serializers.ModelSerializer):
    class Meta:
        model = AttendTable
        fields = '__all__'
