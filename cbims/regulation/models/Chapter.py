# coding: utf-8
from django.db import models
from website.constant import *
from Regulation import *

class Chapter(models.Model):
    code = models.ForeignKey(Regulation, verbose_name = u'规范')
    number = models.IntegerField()
    title = models.CharField('章名', max_length = 255)

    class Meta:
        ordering = ('number',)
        app_label = 'regulation'  
