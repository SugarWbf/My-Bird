"""Bird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import  django01.views as django01
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/', django01.SayHello),#这是django的第一个实例
    url(r'^addDZF/',django01.AddWithDZF), #这是从请求中获取数据的测试,正常的使用
    url(r'^addDZF2/(\d+)/(\d+)/$', django01.AddWithDZF1),  # 这是简化的请求，使用的是正则表达式r'
    #url中name的作用
    url(r'^nameindex/', django01.nameindex),
    url(r'^addDZF5/(\d+)/(\d+)/$', django01.AddWithDZF2, name="usenameTest"),#使用了name后，只要前端有对应的写法，那么网址可以随便改
    #######################################################################################################
    #模板的使用
    url(r'^homemuban/', django01.homemuban)
]
