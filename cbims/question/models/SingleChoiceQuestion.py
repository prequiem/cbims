# coding: utf-8
from django.db import models
from website.constant import *
from regulation.models import Clause

class SingleChoiceQuestion(models.Model):

    # Answer info
    right_choice = models.IntegerField('正确答案', choices = SINGLE_CHOICES)
    explanation = models.TextField('答案解析')
    clause_related = models.ManyToManyField(Clause, verbose_name = u'规范条文', blank = True)
    
    class Meta:
        ordering = ('id', )
        app_label = 'question'

