from django.conf.urls import patterns, include, url
from question.views import *

urlpatterns = patterns('',
    # add single choice question
    url(r'^add/scq/$', singleChoiceQuestion.add),
    )
