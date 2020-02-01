"""quiz URL Configuration

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
from django.conf.urls import include, url
from user.views import home_view,login_view,user_login_fun,main_page_view,register_view,register_user,logout_view,forget_view,forget_password,forget1_view
from myquiz.views import quiz_view,fetch_view,insert_score,fetch_result
urlpatterns = [
    path('',home_view,name='home'),
    path('main_page/',main_page_view,name='quiz'),
    path('quiz/',quiz_view,name='quiz'),
    path('register/',register_view,name='quiz'),
    path('logout/',logout_view,name='quiz'),
    path('forget/',forget_view,name='forget'),
    path('forget1/',forget1_view,name='forget1'),
    path('forget_password/',forget_password,name='forget'),
    path('register_user/',register_user,name='quiz'),
    path('user_login/',login_view,name='login'),
    path('quizz/', fetch_view, name='fetch'),
    path('result/', fetch_result, name='fetch'),
    path('score/', insert_score, name='fetch'),
    path('user_login_fun/',user_login_fun,name='user_login'),
    path('admin/', admin.site.urls),
]
