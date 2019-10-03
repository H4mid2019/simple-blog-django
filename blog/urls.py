from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail')
]
