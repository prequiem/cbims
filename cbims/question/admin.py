#admin.py
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'title', 'text', 'image')




admin.site.register(Choice, ChoiceAdmin)


# Register your models here.
