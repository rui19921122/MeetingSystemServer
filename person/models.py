from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Worker(models.Model):
    worker_name = models.CharField(max_length=20, verbose_name='姓名')
    job = models.ForeignKey('base.Job', verbose_name='工种')
    class_number = models.PositiveSmallIntegerField(verbose_name='班次')
    is_study = models.BooleanField(default=False, verbose_name='是否为学员')

    class Meta:
        verbose_name = '职工(参与点名人员)'

    def __str__(self):
        return self.worker_name

    def get_figure_print_number(self):
        # todo complete this
        return

    def set_figure_print_number(self, value, figure):
        return


class SystemUser(models.Model):
    user = models.OneToOneField(User, verbose_name='登陆用户名')
    department = models.ForeignKey('base.Department', verbose_name='部门')
    name = models.CharField(verbose_name='姓名', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '使用系统人员'
