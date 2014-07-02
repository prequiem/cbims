# coding: utf-8
from django.db import models
from website.constant import *
from Regulation import *

class Chapter(models.Model):
    code = models.ForeignKey(Regulation, verbose_name = u'规范')
    number = models.IntegerField(u'章号')
    title = models.CharField(u'章名', max_length = 255)

    class Meta:
        ordering = ('number',)
        app_label = 'regulation' 

    def __str__(self):
        return self.__unicode__()    
    
    def __unicode__(self):
        return u"%s %s %s"%(self.code, self.number, self.title)

