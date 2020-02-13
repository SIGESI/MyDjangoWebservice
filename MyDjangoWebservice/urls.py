"""MyDjangoWebservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from MyDjangoWebservice import view
from myApp_1 import testdb
from myApp_1.views import time

from myApp_2_login.views import login # or from myApp_2_login import views
from myApp_2_login.views import login_action

from myApp_3_home.views import index,index_action

from myApp_4_algo1.views import algo1, algo1_upload

#Note the path to find the default welcome page
urlpatterns = [
    path('admin/', admin.site.urls),
    #app1 test
    path('hello/',view.hello ),
    path('testdb/',testdb.testdb),
    path('time/', time),

    #app2 login
    path('login/',login),
    path('login_action/',login_action),

    #app3 index
    path('index/', index),
    path('index_action/', index_action),

    #app4 algo1
    path('algo1/', algo1),
    path('algo1_upload/', algo1_upload),

]
