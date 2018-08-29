# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:12:26 2018

@author: lenovo
"""

from django.conf.urls import url
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^import', views.import_data, name='import'),
    url(r'^data', views.data_table),
    url(r'^post', views.post_data, name='post'),
    url(r'^chart', views.chart),
]

