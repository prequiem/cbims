# coding: utf-8
from django.db import models
from account.models import User

class Tag(models.Model):
    name = models.CharField('标签名', max_length = 255, unique = True)
    description = models.TextField('描述', max_length = 255, blank = True)
    parent_tag = models.ForeignKey('self', verbose_name = u'父标签', blank = True, null = True)
    order = models.IntegerField(default = 0)
    picture = models.ImageField('图片', upload_to = 'tag_img/', blank = True, null = True)
    fans = models.ManyToManyField(User, verbose_name = '关注', blank = True)
    is_locked = models.BooleanField('已锁定', default = False)

    class Meta:
        ordering = ( 'order', 'name')
        app_label = 'website'
