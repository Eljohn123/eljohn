"""EljohnList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url 
from EList import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^$', views.StartPage, name = 'startpage'),
    #url(r'^(\d+)/$', views.view_list, name='view_list'),
    #url(r'^(\d+)/add_item$', views.add_item, name='view_list'),
    #url(r'^new$', views.new_list, name='new_list'),

    path('index',views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    path('', views.HomePage, name = 'homepage'),
    path('LoginPage', views.LoginPage, name = 'loginpage'),
    path('SignUpPage', views.SignUpPage, name = 'signuppage'),
    path('DiaryItemList', views.DiaryItemList, name = 'diaryitemlist'),
    path('Archive', views.Archive, name = 'archive'),
]