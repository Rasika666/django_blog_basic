from django.urls import re_path, path
from . import views

app_name = '_accounts'

urlpatterns = [
    re_path(r'^signup/$', views.signup_view, name='signup'),
]