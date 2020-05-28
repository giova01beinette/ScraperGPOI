from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.collect, name='collect'),
    path('admin/', admin.site.urls),
    path('links/', views.make_links, name='links'),
]
