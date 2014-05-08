from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from website.models import Tag
from website.constant import *

class Question(models.Model):

    # status
    status = models.IntegerField('审核状态', choices = PROBLEM_STATUS)

    # basic info 
    number = models.PositiveIntegerField('编号',)
    discipline = models.IntegerField('专业'， choices = DISCIPLINE_CHOICES, default = 0)
    level = models.IntegerField('难度等级', choices = LEVEL_CHOICES, default = 3)

    # additional info
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    # SNS info
    like = models.IntegerField(u'推荐', default = 0)
    dislike = models.IntegerField(u'水题', default = 0)

    # author info
    author = models.ForeignKey(User, verbose_name = '上传者', blank = True, null = True)
    last_modify = models.DateTimeField('最后修改', blank = True, null = True)
    data_timestamp = models.DateTimeField('数据时间戳', blank = True, null = True)


    # submit info
    submit_count = models.PositiveIntegerField('提交次数', default = 0)
    accept_count = models.PositiveIntegerField('通过次数', default = 0)
    wrong_answer = models.PositiveIntegerField('错误答案', default = 0)
    data_count = models.IntegerField('数据个数', default = 0)

    # filter info
    tags = models.ManyToManyField(Tag, verbose_name = u'标签', blank = True)
    source = models.CharField('题目来源', choices = SOURCE_CHOICES, default = '自定义题库')
    code = models.ManyToManyField(Code, verbose_name = u'规范', blank = True)

    class Meta:
        ordering = ('id', )
        app_label = 'question'
