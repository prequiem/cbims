#coding: utf-8
from django.db import models


class Institute(models.Model):
    title = models.CharField(u'单位名称', max_length = 255)
    
    class Meta:
        app_label = 'account'
