# -*- coding:utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea
from captcha.fields import CaptchaField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

from question.models import *

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', '下一步'))
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        exclude = ('status', 'content_type', 'object_id', 'like', 'dislike', 'author', 'last_modify', 'submit_count', 'wrong_count', 'number', )
