#admin.py
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

admin.site.register(Tag, TagAdmin)
