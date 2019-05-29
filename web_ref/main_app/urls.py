from django.urls import path, reverse
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
