from django.conf.urls import patterns, include, url
from website.views import *

urlpatterns = patterns('',
    #
    url(r'^add_tag/$', tag.add),
    )
