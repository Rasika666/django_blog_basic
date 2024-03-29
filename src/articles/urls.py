from django.urls import re_path
from . import views

app_name = '_articles'

urlpatterns = [
    re_path(r'^$', views.article_list, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail')
]