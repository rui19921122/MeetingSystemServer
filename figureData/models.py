from django.db import models


# Create your models here.
class FigurePrint(models.Model):
    value = models.CharField(max_length=513, verbose_name='指纹模型')
    user = models.ForeignKey('person.Worker', verbose_name='职工')
    name = models.CharField(max_length=5, choices=(
        ('左手大拇指', '左手大拇指'),
        ('左手食指', '左手食指'),
        ('左手中指', '左手中指'),
        ('左手无名指', '左手无名指'),
        ('左手小拇指', '左手小拇指'),
        ('右手大拇指', '右手大拇指'),
        ('右手食指', '右手食指'),
        ('右手中指', '右手中指'),
        ('右手无名指', '右手无名指'),
        ('右手小拇指', '右手小拇指'),
    ))
    weight = models.PositiveSmallIntegerField(verbose_name='使用权重', default=1)

    def __str__(self):
        return '{name}的{figure}'.format(
            name=self.user.worker_name,
            figure=self.name)

    class Meta:
        verbose_name = '指纹数据'


class FigureUseRecord(models.Model):
    """
    指纹使用记录
    """
    time = models.TimeField(verbose_name='使用时间')
    raw_data = models.CharField(max_length=513, verbose_name='请求指纹模型')
    match_figure_print = models.ForeignKey(
        'figureData.FigurePrint',
        verbose_name='匹配指纹')

    class Meta:
        verbose_name = '匹配模型'


