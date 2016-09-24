from django.db import models


# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=20, verbose_name='部门名称')
    is_managed = models.BooleanField(default=False, verbose_name='是否为管理部门',
                                     help_text='如果为管理部门，则可以查询所有车间点名会情况')
    can_modify_class_plan = models.BooleanField(default=False,
                                                verbose_name='是否可更改班计划表',
                                                help_text='由于班计划表已暂时移除，因此此选项暂时无用'
                                                )
    can_add_figure_data = models.BooleanField(default=False,
                                              verbose_name='是否可添加指纹')
    can_delete_figure_data = models.BooleanField(default=False,
                                                 verbose_name='是否可删除指纹')

    class Meta:
        verbose_name = '部门'

    def __str__(self):
        return self.department_name


class Job(models.Model):
    job_name = models.CharField(max_length=20, verbose_name='职名')
    should_attend_meeting = models.BooleanField(verbose_name='是否参与点名')
    department = models.ForeignKey('base.Department', verbose_name='职位')

    class Meta:
        verbose_name = '职务'

    def __str__(self):
        return self.job_name


class ClassNumberTable(models.Model):
    date = models.DateField()
    day_number = models.SmallIntegerField(choices=(
        (1, '白班'), (2, '夜班')
    ))
    class_number = models.SmallIntegerField(choices=(
        (1, '一班'), (2, '二班'), (3, '三班'), (4, '四班')
    ))

    class Meta:
        unique_together = (('date', 'day_number'),)
