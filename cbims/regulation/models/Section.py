# coding: utf-8
from django.db import models
from website.constant import *
from Chapter import *

class Section(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name = u'章')
    number = models.IntegerField(u'节号')
    title = models.CharField(u'节名', max_length = 255)

    class Meta:
        ordering = ('number',)
        app_label = 'regulation'
    
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"%s %s %s"%(self.chapter, self.number, self.title)
