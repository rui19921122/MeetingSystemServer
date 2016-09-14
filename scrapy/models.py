from django.db import models


# Create your models here.

class ScrapyTable(models.Model):
    create_person = models.ForeignKey('person.SystemUser', verbose_name='录入人')
    create_time = models.DateTimeField(verbose_name='录入时间', auto_now=True)
    url = models.URLField(verbose_name='路局链接')

    class Meta:
        verbose_name = '班前预想表'

    def __str__(self):
        return self.attendtable + '的班前预想表'


class ScrapyContent(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    index = models.PositiveSmallIntegerField(verbose_name='编号')
    scrapy_table = models.ForeignKey('scrapy.ScrapyTable', verbose_name='预想表')

    def __str__(self):
        return self.scrapy_table + self.title

    class Meta:
        verbose_name = '条目内容'
