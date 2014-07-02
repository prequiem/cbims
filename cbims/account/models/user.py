#coding: utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from website.constant import *
from institute import *
import datetime

class CbimsUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Users must have a email address')
        
        user = self.model(
            email = CbimsUserManager.normalize_email(email),
            username = username,
            is_staff = False,
            is_active = True,
            is_superuser = False,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, 
            username,
            password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    # auth information
    username = models.CharField(verbose_name = u'用户名', max_length = 100, unique = True, db_index = True)
    email = models.EmailField(verbose_name = u'邮箱地址', max_length = 255, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    # admin information
    last_login_datetime = models.DateTimeField(u'最后登录时间', auto_now_add = True, null = True)
    upload_datetime = models.DateTimeField(u'允许上传题目的时间', auto_now_add = True)
    verified = models.BooleanField(u'通过验证', default = False)
    ipaddress = models.IPAddressField(u'最后一次登录地址', blank = True, null = True)

    # personal information
    province = models.IntegerField(u'省份', choices = PROVINCE_CHOICES, default = 1, blank = True)
    institute = models.ForeignKey(Institute, verbose_name = u'单位', blank = True, null = True)
    name = models.CharField(u'真实姓名', max_length = 16, blank = True, null = True)
    qq = models.CharField(u'QQ', max_length = 16, blank = True, null = True)
    mobile = models.CharField(u'手机号', max_length = 20, blank = True, null = True)
    birthday = models.DateField(u'生日', blank = True, null = True)
    
    # statistic information
    score = models.IntegerField(u'积分', default = 0)
    answered_count = models.PositiveIntegerField(u'通过的题数', default = 0)
    level = models.IntegerField(u'用户等级', choices = USER_LEVEL_CHOICES, default = 1)
    upload_count = models.IntegerField(u'发布的题数', default = 0)

    # SNS
    gender = models.CharField(u'性别', max_length = 1, choices = GENDER_CHOICES, default = 'F')
    avatar = models.CharField(u'头像', max_length = 100, blank = True, null = True) 
    avatar_datetime = models.DateTimeField(auto_now_add = True)
    status = models.CharField(u'状态', blank = True, max_length = 255, null = True)
    privacy = models.IntegerField(u'隐私', choices = PRIVACY_CHOICES, default = 0)


    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email']

    objects = CbimsUserManager()

    class Meta:
        app_label = 'account'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username


