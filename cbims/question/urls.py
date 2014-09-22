from django.conf.urls import patterns, include, url
from question.views import *

urlpatterns = patterns('',
    #
    url(r'^add_single_choice_question/$', singleChoiceQuestion.add),
    )
