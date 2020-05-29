from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.collect, name='collect'),
    path('links/', views.make_links, name='links'),
]
