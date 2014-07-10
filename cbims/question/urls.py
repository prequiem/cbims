from django.conf.urls import patterns, include, url
from question.views import *

urlpatterns = patterns('',
    #
    url(r'^add/$', question.add),
    )
