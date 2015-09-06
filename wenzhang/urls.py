#coding:utf-8
from django.conf.urls import patterns,url
from wenzhang.views import RSSFeed
urlpatterns = patterns('',
        #name的作用是给url和get_absolute_url调用的
        url(r'^$','wenzhang.views.home',name='home'),
        url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'wenzhang.views.detail', name="detaild"),#每篇文章
        url(r'^articleClassfi/(?P<classfi>\w+)/$', 'wenzhang.views.classfiDetail', name="classfiDetail"),#每个分类页下面的文章
        url(r'^articleTag/(?P<tag>\w+)/$', 'wenzhang.views.tagDetail', name="tagDetail"),#每个标签页下面的文章
        url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/$','wenzhang.views.archive_month',name="archive_month"),#按月归档
        url(r'^archive/$','wenzhang.views.archive',name="archive"),#归档
        url(r'^about/$','wenzhang.views.about',name="about"),#关于我
        url(r'^message/$','wenzhang.views.message',name="message"),#留言
        url(r'^feed/$', RSSFeed(), name = "RSS"),
        url(r'^search/$','wenzhang.views.blog_search', name = "search"),#按文章标题搜索
        )