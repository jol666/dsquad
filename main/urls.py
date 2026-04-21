from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
