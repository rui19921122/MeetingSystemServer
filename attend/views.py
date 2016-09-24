import datetime

from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response

from person.models import Worker
from person.serializers import WorkerSer
from .serializers import AttendPersonSer, AttendTableSer
from .models import AttendTable, AttendPerson, ClassNumberTable
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from permission import OnlyOwnerOrSuperuserCanReadAndEdit


# Create your views here.
class GetAttendTableView(generics.RetrieveAPIView):
    """
    根据时间与类型返回出勤表
    :return {'all_workers':worker[],'attend_workers':worker[]}
    """
    serializer_class = AttendTableSer
    permission_classes = [IsAuthenticated, OnlyOwnerOrSuperuserCanReadAndEdit]

    def retrieve(self, request: Request, *args, **kwargs):
        attend_table = self.get_object(*args, **kwargs)
        data = self.get_serializer(attend_table)
        return Response(data={'attend_table': self.get_serializer(attend_table).data,
                              'attend_workers': AttendPersonSer(
                                  attend_table.attendperson_set.all(),
                                  many=True, context={'request': request}
                              ).data,
                              'all_workers': WorkerSer(
                                  Worker.objects.filter(department_id=kwargs.get('department')), many=True).data
                              })

    def get_object(self, *args, **kwargs):
        department_id = kwargs.get('department')
        date_string = kwargs.get('date').split('-')  # 解析date参数
        year = int(date_string[0])
        month = int(date_string[1])
        day = int(date_string[2])
        date = datetime.date(year, month, day)
        day_number = kwargs.get('day_number')
        try:
            obj = AttendTable.objects.get(
                department_id=department_id,
                date=date,
                day_number=day_number
            )
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            class_number = ClassNumberTable.objects.get(date=date,
                                                        day_number=day_number).class_number
            new = AttendTable(
                department_id=department_id,
                date=date,
                day_number=day_number,
            )
            new.save()
            new.auto_add_attend_person()
            return new


class ReplaceAttentionWorkerView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendPersonSer
    permission_classes = [IsAuthenticated, OnlyOwnerOrSuperuserCanReadAndEdit]
    queryset = AttendPerson

    def delete(self, request: Request, *args, **kwargs):
        pass

    def put(self, request: Request, *args, **kwargs):
        replace_worker = Worker.objects.get(pk=request.data.get('worker'))
