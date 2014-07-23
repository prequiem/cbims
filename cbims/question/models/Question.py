#coding: utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from website.models import Tag
from website.constant import *
from account.models import User

class Question(models.Model):

    # status
    status = models.IntegerField('审核状态', choices = PROBLEM_STATUS)

    # basic info 
    discipline = models.IntegerField('专业', choices = DISCIPLINE_CHOICES, default = 0)
    level = models.IntegerField('难度等级', choices = QUESTION_LEVEL_CHOICES, default = 3)

    # additional info
    limit = ((models.Q(app_label = 'question', model = 'singlechoicequestion'), u"选择题"),)
    content_type = models.ForeignKey(ContentType, verbose_name = u'题目类型', choices = limit)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    # SNS info
    like = models.IntegerField(u'推荐人数', default = 0)
    dislike = models.IntegerField(u'不推荐人数', default = 0)

    # author info
    author = models.ForeignKey(User, verbose_name = '上传者', blank = True, null = True)
    last_modify = models.DateTimeField('最后修改', blank = True, null = True)

    # submit info
    submit_count = models.PositiveIntegerField('提交次数', default = 0)
    wrong_count = models.PositiveIntegerField('错误次数', default = 0)

    # filter info
    tags = models.ManyToManyField(Tag, verbose_name = u'标签', blank = True)
    source = models.IntegerField('题目来源', choices = SOURCE_CHOICES, default = 0)
    number = models.PositiveIntegerField('编号', blank = True, null = True)

    class Meta:
        ordering = ('id', )
        app_label = 'question'
