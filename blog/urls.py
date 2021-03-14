from django.urls import path
from . import views

urlpatterns = [
    # pattern will be handled by views.home file
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
