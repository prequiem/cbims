# coding: utf-8
from django.db import models
from website.constant import *
from Chapter import *

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name = u'章')
    number = models.IntegerField()
    title = models.CharField('节名', max_length = 255)

