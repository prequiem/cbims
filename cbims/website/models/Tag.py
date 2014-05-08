# coding: utf-8

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField('标签名', max_length = 255, unique = True)
    description = models.CharField('描述', max_length = 255, blank = True)
    tag_type = models.CharField('标签类型', max_length = 255, blank = True)
    parent_tag = models.ForeignKey('self', verbose_name = u'父标签', blank = True, null = True)
    order = models.IntegerField(default = 0)
    picture = models.URLField('图片', blank = True)
    fans = models.ManyToManyField(User, verbose_name = '关注', blank = True)
    is_locked = models.BooleanField('已锁定', default = False)

    class Meta:
        ordering = ('tag_type', 'order', 'name')
        app_label = 'website'
                                                            
    def n_problems(self):
        return self.problem_set.filter(status = 1).count()
                                                                                
    def __str__(self):
        return self.__unicode__()
                                                                                                
    def __strstr__(self):                                                                                return self.__unicode__()
                                                                                                     def __unicode__(self):                                                                               return u'%s %s'%(self.tag_type, self.name)
