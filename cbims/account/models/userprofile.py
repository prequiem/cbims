from django.db import models
from django.contrib.auth.models import User
from website.constant import *
import datetime


class UserProfile(models.Model):
    #auth
    user = models.ForeignKey(User, unique = True, verbose_name = '用户的额外信息')
    
    # admin information
    upload_datetime = models.DateTimeField(u'允许上传题目的时间', auto_now_add = True)
    verified = models.BooleanField(u'通过验证', default = False)
    ipaddress = models.IPAddressField(u'最后一次登录地址', blank = True, null = True, default = '')

    # basic information
    province = models.CharField(max_length = 50, choices = PROVINCE_CHOICES, default = u'北京', blank = True)
    institute = models.ForeignKey(Institute, verbose_name = u'单位'， blank = True, null = True)

    name = models.CharField('真实姓名', max_length = 16, blank = True)
    qq = models.CharField('QQ', max_length = 16, blank = True)
    mobile = models.CharField('手机号', max_length = 20, blank = True)
    birthday = models.DateField('生日', blank = True, null = True)
    gender = models.CharField('性别', maxlength=1, choices=GENDER_CHOICES, radio_admin=True, default='M')
    
    # statistic information
    score = models.IntegerField('积分', default = 0)
    accept_count = models.PositiveIntegerField('通过题目数', default = 0)
    level = models.IntegerField('天梯等级', choices = LEVEL_CHOICES, default = 1)
    solution_count = models.IntegerField('发布的题解个数', default = 0)
    user = models.OneToOneField(User, related_name="get_profile")

    # SNS
    gender = models.BooleanField('性别', choices = ((False, '男'),(True, '女')), default=False)
    avatar = models.CharField('头像', max_length = 100, blank = True) 
    avatar_datetime = models.DateTimeField(auto_now_add = True)
    status = models.CharField('状态', blank = True, max_length = 255)
    privacy = models.IntegerField('隐私', choices = PRIVACY_CHOICES, default = 0)
