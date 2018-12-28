"""payrollproject3 URL Configuration

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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from paymentapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('mylogin',views.mylogin,name="mylogin"),
url(r'^accounts/login', auth_views.login, {'template_name': 'login.html'}, name='login'),
url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, name='logout'),
path('hr_pwd_chg',views.hr_pwd_chg,name="hr_pwd_chg"),
path('hr_otpvalid',views.hr_otpvalid,name="hr_otpvalid"),
path('hr_login',views.hr_login,name="hr_login"),
path('finance_pwd_chg',views.finance_pwd_chg,name="finance_pwd_chg"),
path('finance_otpvalid',views.finance_otpvalid,name="finance_otpvalid"),
path('finance_login',views.finance_login,name="finance_login"),
path('empdetails',views.empdetails,name="empdetails"),
path('activate',views.activate,name="activate"),
path('empactive',views.empactive,name="empactive"),
path('empbasicupdate',views.empbasicupdate,name="empbasicupdate"),
path('empleavesupdate',views.empleavesupdate,name="empleavesupdate"),

path('basicpay',views.basicpay,name="basicpay"),


path('emp_pwd_chg',views.emp_pwd_chg,name="emp_pwd_chg"),
path('emp_otpvalid',views.emp_otpvalid,name="emp_otpvalid"),
path('emp_login',views.emp_login,name="emp_login"),
path('accountupdate',views.accountupdate,name='accountupdate'),
]
