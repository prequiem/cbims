# coding: utf-8
from django.db import models
from website.constant import *

class Regulation(models.Model):
    title = models.CharField(u'规范名称', max_length = 255)
    serial_number = models.CharField(u'规范编号', max_length = 255)
    year = models.IntegerField(u'发布年份')
    level = models.IntegerField(u'规范级别', choices = REGULATION_LEVEL_CHOICES, default = 0)
    is_locked = models.BooleanField(u'是否已锁', default = False)

    class Meta:
        ordering = ('serial_number',)
        app_label = 'regulation'
