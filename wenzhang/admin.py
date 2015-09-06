#coding:utf-8
from django.contrib import admin
from wenzhang.models import Article,Author,Tag,Classification
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')  #设置作者类显示的表头
    search_fields = ('name',)                    #添加按姓名查询的功能
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'publish_time','classification')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'        #设置时间过滤器
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)         #水平显示的过滤器
#以上内容均为对显示内容的修饰

#以下注释是tinymce富文本编辑器，打开注释就能使用
#    class Media:
#        js = (
#        '/static/tinymce/tinymce.min.js',
#        '/static/tinymce/config.js',
#        )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Classification)

