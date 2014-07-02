# coding: utf-8
from django.db import models
from website.constant import *
from Section import *
from account.models import User

class Clause(models.Model):
    section = models.ForeignKey(Section, verbose_name = u'节')
    number = models.IntegerField(u'条文号')
    content = models.TextField(u'条文内容')
    explanation = models.TextField(u'条文解释')
    is_mandatory = models.BooleanField(u'是否强条', default = False)
    creater = models.ForeignKey(User, verbose_name = '创建人', related_name = 'first')
    last_editor = models.ForeignKey(User, verbose_name = '最后编辑人', related_name = 'last')
    
    class Meta:
        ordering = ('number',)
        app_label = 'regulation'  
