from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as authviews
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'account'

urlpatterns = [
    url(r'^$', views.profile, name='home'),
    url(r'^login/$', csrf_exempt(views.login_user),name='login'),
    url(r'^logout/$', views.logout_user,name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^forgotpassword/$', views.forgot_password, name='forgotpassword'),
    url(r'^changepassword/$', views.change_password, name='changepassword'),
    url(r'^changepassword/$', views.change_password, name='changepassword'),
    url(r'^editdetails/$', views.edit_details, name='editdetails'),
]