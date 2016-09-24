from django.db import models
from base.models import ClassNumberTable
import datetime

# Create your models here.
from person.models import Worker


class AttendTable(models.Model):
    department = models.ForeignKey('base.Department', verbose_name='部门')
    day_number = models.PositiveSmallIntegerField(choices=(
        (1, '白班'),
        (2, '夜班')
    ),
        verbose_name='班别')
    date = models.DateField(verbose_name='日期')
    create_time = models.DateTimeField(verbose_name='创建时间', blank=True,
                                       auto_created=True)
    lock_time = models.TimeField(verbose_name='锁定时间(开始时间)', null=True, blank=True)
    lock_person = models.ForeignKey('person.SystemUser', verbose_name='锁定人', null=True, blank=True)
    end_time = models.TimeField(verbose_name='结束时间', null=True, blank=True)
    scrapy_table = models.OneToOneField('scrapy.ScrapyTable', null=True, blank=True, verbose_name='班前预想表')

    def save(self, *args, **kwargs):
        # 当创建出勤表时，如未指定
        if not self.id:
            self.create_time = datetime.datetime.now()
        super(AttendTable, self).save(*args, **kwargs)

    def __str__(self):
        return "{department} {year}年{month}月{day}日的{day_number}点名会".format(
            department=self.department.department_name,
            year=self.date.year,
            month=self.date.month,
            day=self.date.day,
            day_number='白班' if self.day_number == 1 else '夜班'
        )

    def auto_add_attend_person(self):
        workers = Worker.objects.filter(department=self.department,
                                        class_number=self.get_class_number()
                                        )
        for worker in workers:
            AttendPerson.objects.create(worker=worker,
                                        attend_table=self,
                                        is_study=worker.is_study,
                                        job=worker.job)

    def get_class_number(self):
        return ClassNumberTable.objects.get(date=self.date,
                                            day_number=self.day_number,
                                            ).class_number

    class Meta:
        verbose_name = '出勤表'
        unique_together = ('date', 'department', 'day_number')


class AttendPerson(models.Model):
    worker = models.ForeignKey('person.Worker', verbose_name='职工')
    job = models.ForeignKey('base.Job', verbose_name='职位名')
    is_study = models.BooleanField(verbose_name="是否为学员", default=False)
    off_record = models.OneToOneField(
        'figureData.FigureUseRecord',
        verbose_name='退勤记录',
        related_name='off_record',
        null=True,
        blank=True
    )
    on_record = models.OneToOneField(
        'figureData.FigureUseRecord',
        verbose_name='出勤记录',
        related_name='on_record',
        null=True,
        blank=True
    )
    attend_table = models.ForeignKey('attend.AttendTable',
                                     verbose_name='出勤表')

    @property
    def department(self):
        return self.job.department

    def __str__(self):
        return "{} {}".format(self.attend_table, self.worker)

    class Meta:
        verbose_name = '出勤详细'