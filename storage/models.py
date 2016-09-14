from django.db import models


# Create your models here.

class Video(models.Model):
    file = models.FileField(upload_to='video')
    attend_table = models.ForeignKey('attend.AttendTable', verbose_name='出勤表')
    upload_time = models.DateTimeField(verbose_name='上传时间')
