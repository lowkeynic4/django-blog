#coding:utf-8
from django.conf.urls import include,url,patterns
from django.contrib import admin
from wenzhang.models import Article
#from wenzhang.views import RSSFeed

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('wenzhang.urls')),



)
