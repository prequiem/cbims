from django.contrib import admin
from models import *
# -*- coding: utf-8 -*-
# Register your models here.

class RegulationAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial_number', 'year', 'level', 'is_locked')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('code', 'number', 'title')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'number', 'title')

class ClauseAdmin(admin.ModelAdmin):
    list_display = ('section', 'number', 'content', 'explanation', 'is_mandatory', 'creater', 'last_editor')


admin.site.register(Regulation, RegulationAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Clause, ClauseAdmin)
