from django.conf.urls import patterns, include, url
from regulation.views import *

urlpatterns = patterns('',
    # 
    url(r'^add/$', regulation.add),
    )
