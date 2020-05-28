from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('search', views.category, name="base"),
    path('', views.home, name='compatech-home'),
]
