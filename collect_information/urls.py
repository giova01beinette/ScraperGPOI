from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('empty/', views.empty_table_prodotti, name='empty_table'),
    path('admin/', admin.site.urls),
    path('links/', views.make_links, name='links'),
    path('eprice/', views.scrape_eprice, name='links'),
    path('unieuro/', views.scrape_unieuro, name='unieuro'),
    path('ollostore/', views.scrape_ollostore, name='ollostore'),
    path('euronics/', views.scrape_euronics, name='euronics'),
    #path('trony/', views.amazon_links, name='amazonLinks'),
]
