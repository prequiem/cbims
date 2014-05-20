from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

from settings import STATIC_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cbims.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/', include('question.urls')),
)
