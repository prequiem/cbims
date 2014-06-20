# -*- coding: utf-8 -*-

from django.db import models
from website.constant import SINGLE_CHOICES
from SingleChoiceQuestion import *

class Choice(models.Model):
    question = models.ForeignKey(SingleChoiceQuestion)
    title = models.IntegerField(u'答案选项', choices = SINGLE_CHOICES)
    text = models.CharField(u'选项内容', max_length = 255, blank = False, null = True)
    image = models.ImageField(upload_to = 'media/uploads/')

