# coding=utf-8
"""Url handlers for user map."""

from django.conf.urls import url

from user_map import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
