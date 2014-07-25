# coding: utf-8
from django.db import models
from website.constant import *
from regulation.models import Clause

class SingleChoiceQuestion(models.Model):

    # Answer info
    content = models.TextField(u'题目内容')
    right_choice = models.IntegerField(u'正确答案', choices = SINGLE_CHOICES)
    explanation = models.TextField(u'答案解析')
    clause_related = models.ManyToManyField(Clause, verbose_name = u'规范条文', blank = True)
    
    class Meta:
        ordering = ('id', )
        app_label = 'question'

        

