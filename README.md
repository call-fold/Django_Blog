# Django Blog
## 传送门: [call-fold之家](http://www.slfweb.com)
![my_blog](https://cloud.githubusercontent.com/assets/12811161/20725349/772384c2-b6ac-11e6-9ae0-cf019f6dc8cc.png)
</br>

## Update

 + 2017.02.13: **[实验室-电影搜索器](http://slfweb.com/movie_search/)**, 定时爬取全站数据, 清洗后从Redis中访问, 如没有, 则在线爬取查询
 + 2017.01.11: 为站点添加SSL, http -> https
 + 2017.01.09: 解决markdown换行问题
 + 2017.01.01: 增加AJAX功能, jQuery实现
 + 2016.11.26: 增加**[实验室-电影搜索器](http://slfweb.com/movie_search/)**, 具体的项目请参考**[MovieCrawler](https://github.com/call-fold/MovieCrawler)**
 + 2016.08.21: 增加sites站点
 + 2016.08.21: 增加nginx和uWSGI

## Requirement

 - Python (3.4.3)
 - pyenv
 - Pure.css
 - MySQL
 - nginx
 - jQuery
 - Redis
 
## Pip List

 - Django (1.8.2)
 - django-disqus (0.5)
 - Markdown (2.6.6)
 - PyMySQL (0.7.2)
 - uWSGI (2.0.13.1)
 - redis (2.10.5)
 
## Tips

 - 本博客基本参考Andrew_liu的[Django博客教程](https://www.gitbook.com/book/andrew-liu/django-blog/details)进行搭建
 - 数据库从SQLite3换为MySQL
 - 使用pyenv管理python环境, 具体参考[这篇文章](http://www.cnblogs.com/npumenglei/p/3719412.html)
 - CSS采用yahoo的Pure, 具体配置参考[Pure主页](http://purecss.io/)
 - 开发环境选择JetBrains的[PyCharm](https://www.jetbrains.com/pycharm/)
 - 部署方式: web应用(Django)+web应用服务器(uWSGI)+web服务器软件(nginx), 动态请求由uWSGI传递给Django, 静态请求由nginx处理
 
## 待解决问题

 + Disqus异步加载有些问题
 + ~~耗时长的搜索项, 有些不稳定~~
 + ~~电影搜索时, nginx会504超时, 待解决~~
 + ~~电影搜索时, 下方的disqus不要重载~~


