# django-blog
1. 支持markdown语法
2. 安装了bootstrap_admin后台，后台地址http://127.0.0.1:8000/admin/，账号密码都是nick
3. 添加多说评论
4. 添加jiathis分享按钮
5. 添加cnzz统计，并显示在footer中
6. 采用JQcloud实现标签云功能
7. 添加新浪微博秀
8. 支持tinymce富文本编辑器，但是和markdown冲突，我将调用tinymce的地方在admin.py中注释掉了
9. url路由没有都写在主url.py中，而是写在了app的url.py中，符合复用思想。
10. 使用了默认的sqlite数据库，但是mysql数据的配置也写了，但是注释起来了，可以使用。

必看和最初看the django book
http://djangobook.py3k.cn/2.0/

自强学堂，django book精简版
http://www.ziqiangxuetang.com/django/django-tutorial.html

简单blog
http://andrew-liu.gitbooks.io/django-blog/content/index.html

简单blog
http://muker.net/django-blog-two.html

也是一个简单blog程序
http://django-web-app-book.wanqingwong.com/

@models.permalink讲解，关于get_absolute_url()
http://my.oschina.net/ranvane/blog/336817?p=1

我的这个blog是从以下项目改善而来
https://github.com/tmacjx/my_site

正则表达式查询，url.py中需要用到
http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

　　以上的资料就是写出这个blog程序的所有资料，其他就是遇到问题时去baidu&google了，在这提一点，我在写这个程序的过程中遇到的很多问题都是在stackoverflow中知道的，希望我和大家以后都多多使用。
　　还有就是我的这个程序中的文章是我从freebuf中随便截取来的，只为有点文字，别无他用！

　　以下就是我所用到的包
* bootstrap-admin==0.3.6
* Django==1.8.4
* Markdown==2.6.2

下面是我将这个程序放在了新浪sea上，没有实名认证，所以上面有个提示
http://tenshine.sinaapp.com

以下是github地址：
https://github.com/lowkeynic4/django-blog
![](http://7xljat.com1.z0.glb.clouddn.com/QQ截图20150906100936.jpg)

