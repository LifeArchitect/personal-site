"""psw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from pswapp import views

urlpatterns = [ # 13 of 38
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'posts/$', views.posts_home, name='posts_home'),
    url(r'posts/create/$', views.post_create, name='post_create'),
    url(r'posts/detail/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'posts/list/$', views.post_list, name='post_list'),
    url(r'posts/update/(?P<id>\d+)/$', views.post_update, name='post_update'),
    url(r'posts/delete/(?P<id>\d+)/$', views.post_delete, name='post_delete'),

]
