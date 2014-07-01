#admin.py
# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'title', 'text', 'image')

class SingleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('right_choice', 'explanation')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('status', 'number', 'discipline', 'level', 'content_type', 'author', 'source')

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(SingleChoiceQuestion, SingleChoiceQuestionAdmin)
admin.site.register(Question, QuestionAdmin)
# Register your models here.
