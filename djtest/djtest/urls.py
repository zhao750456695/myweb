# coding=utf-8
"""djtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from organization.views import OrgView
from django.views.static import serve
from djtest.settings import MEDIA_ROOT
from users.views import IndexView, page_error, page_not_found

handler404 = page_not_found
handler500 = page_error
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name='index'),
    # url('^login/$', user_login, name='login'), # 指向函数，而不是调用，所以没有括号
    url('^login/$', LoginView.as_view(), name='login'), # 这里是方法，有括号
    url('^logout/$', LogoutView.as_view(), name='logout'),  # 这里是方法，有括号

    url('^index/$', IndexView.as_view(), name='index'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'), # ?P(p是大写的)提取一个变量作为参数 <active_code>是变量名，再后面是正则表达式
    url('^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 生产环境static url配置
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace='courses')),
    #url(r'^teacher/', include('teachers.urls', namespace='teachers')),
    url(r'^users/', include('users.urls', namespace='users')),

]
