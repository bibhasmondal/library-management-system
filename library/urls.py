from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'library'

urlpatterns = [
    url(r'^$', views.LibHome, name='home'),
    url(r'^index/$', views.BookIndex.as_view(), name='library'),
    url(r'^book/(?P<id>[0-9]+)/$', views.BookDetail, name='detail'),
    url(r'^book/edit/(?P<pk>[0-9]+)/$', login_required(views.BookEdit.as_view()), name='edit'),
    url(r'^new/$', views.NewForm, name='new'),
    url(r'^add/$', login_required(views.BookAdd.as_view()), name='add'),
    url(r'^request/(?P<id>[0-9]+)/issue/$', views.IssueBook, name='issue'),
    url(r'^request/(?P<id>[0-9]+)/return/$', views.ReturnBook, name='return'),
    url(r'^request/(?P<id>[0-9]+)/collect/$', views.CollectBook, name='collect'),
    url(r'^request/(?P<id>[0-9]+)/undoreturn/$', views.UndoReturn, name='undoreturn'),
    url(r'^search/$', views.Search, name='search'),
    url(r'^admin_dashboard/$', views.adminDash, name='admin_dash'),
    url(r'^dashboard/$', views.UserDashboard, name='user_dashboard'),
    url(r'^del_request/(?P<id>\d+)/$', views.deleteRequest, name="delete_request"),
]
